from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    # Delete all rows in a table
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    # Seed restaurants
    dominion_pizza = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
    pizza_hut = Restaurant(name='Pizza Hut', address='Westgate Mall, Mwanzi Road, Nrb 100')

    # Seed pizzas
    cheese_pizza = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
    pepperoni_pizza = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')

    # Add Restaurants and Pizzas to session
    db.session.add_all([dominion_pizza, pizza_hut, cheese_pizza, pepperoni_pizza])
    db.session.commit()

    # Seed RestaurantPizzas
    dominion_cheese_pizza = RestaurantPizza(price=15, restaurant=dominion_pizza, pizza=cheese_pizza)
    dominion_pepperoni_pizza = RestaurantPizza(price=18, restaurant=dominion_pizza, pizza=pepperoni_pizza)
    pizza_hut_cheese_pizza = RestaurantPizza(price=12, restaurant=pizza_hut, pizza=cheese_pizza)
    pizza_hut_pepperoni_pizza = RestaurantPizza(price=20, restaurant=pizza_hut, pizza=pepperoni_pizza)

    # Add RestaurantPizzas to session
    db.session.add_all([dominion_cheese_pizza, dominion_pepperoni_pizza, pizza_hut_cheese_pizza, pizza_hut_pepperoni_pizza])
    db.session.commit()
