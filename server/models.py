# server/models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    serialize_only = ('id', 'name', 'address', 'restaurant_pizzas',)
    serialize_rules = ('-restaurant_pizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship("RestaurantPizza", back_populates="restaurant")


    @validates('name')
    def validate_name(self, key, name):
        if len(name.strip()) == 0:
            raise ValueError("Name cannot be empty.")
        return name

    def __repr__(self):
        return f'<Restaurant ID: {self.id}, Name: {self.name}, Address: {self.address}>'

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    serialize_only = ('id', 'name', 'ingredients',)
    serialize_rules = ('-restaurant_pizzas.pizza',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)

    restaurant_pizzas = db.relationship("RestaurantPizza", back_populates="pizza")

    def __repr__(self):
        return f'<Pizza ID: {self.id}, Name: {self.name}, Ingredients: {self.ingredients}>'

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    serialize_only = ('id', 'price', 'restaurant_id', 'pizza_id',)
    serialize_rules = ()

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    restaurant = db.relationship("Restaurant", back_populates="restaurant_pizzas")
    pizza = db.relationship("Pizza", back_populates="restaurant_pizzas")

    @validates('price')
    def validate_price(self, key, price):
        if not 1 <= price <= 30:
            raise ValueError("Price must be between 1 and 30.")
        return price

    def __repr__(self):
        return f'<RestaurantPizza ID: {self.id}, Price: {self.price}, Restaurant ID: {self.restaurant_id}, Pizza ID: {self.pizza_id}>'
