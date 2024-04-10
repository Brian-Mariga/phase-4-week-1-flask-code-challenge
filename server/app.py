#!/usr/bin/env python3
# server/app.py

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Phase 4 Code Challenge: Pizza Restaurants</h1>'

@app.route('/restaurants')
def get_restaurants():
    if restaurants := [restaurant.to_dict() for restaurant in Restaurant.query.all()]:
        return make_response(restaurants, 200)
    else:
        return make_response(jsonify({"error": "No restaurant found"}), 404)

@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def restaurant_by_id(id):
    if restaurant := Restaurant.query.filter(Restaurant.id == id).first():
        if request.method == 'GET':
            restaurant_dict = restaurant.to_dict()
            return make_response(restaurant_dict, 200)
        elif request.method == 'DELETE':
            db.session.delete(restaurant)
            db.session.commit()
            return make_response({'message': 'Restaurant successfully deleted'}, 200)

    else:
        return make_response(jsonify({"error": f"Restaurant of ID {id} not found"}), 404)

@app.route('/pizzas')
def get_pizzas():
    if pizzas := [pizza.to_dict() for pizza in Pizza.query.all()]:
        return make_response(pizzas, 200)
    else:
        return make_response({'message': 'No pizza found'}, 404)

@app.route('/restaurant_pizzas', methods=['POST'])
def add_restaurant_pizzas():
    data = request.json
    if not data or 'price' not in data or 'pizza_id' not in data or 'restaurant_id' not in data:
        return make_response(jsonify({"errors": "Invalid request data."}), 400)

    price = data['price']
    pizza_id = data['pizza_id']
    restaurant_id = data['restaurant_id']

    if not (1 <= price <= 30):
        return make_response(jsonify({"errors": "Price must be between 1 and 30."}), 400)

    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return make_response(jsonify({"errors": "Restaurant not found."}), 404)

    pizza = Pizza.query.get(pizza_id)
    if not pizza:
        return make_response(jsonify({"errors": "Pizza not found."}), 404)

    restaurant_pizza = RestaurantPizza(price=price, restaurant_id=restaurant_id, pizza_id=pizza_id)
    db.session.add(restaurant_pizza)
    db.session.commit()

    return make_response(jsonify(pizza.to_dict()), 201)



if __name__ == '__main__':
    app.run(port=5555, debug=True)