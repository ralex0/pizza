"""
To-Do: 
*Move menu to a stored file and simply import them here rather than
storing data in code. Shoudln't really use __init__ as metadata, but it works. 

*Maybe (probably) use pandas to handle menu?

"""
from pizza import Pizza

toppings = ['onions', 'pepperoni', 'tomato', 'basil']
cheeses = ['mozerella']
sauces = ['tomato', 'pesto']

# Defining some common pizzas. Add your favorite pizza to the list!
pizza_classic = Pizza(name='The Classic', toppings='pepperoni')
pizza_ron = Pizza(name="Ron's Favorite", sauce='pesto', toppings=['pepperoni', 'tomato', 'basil'])