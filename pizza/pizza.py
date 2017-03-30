"""
To-Do (in progress): transform toppings from a simple identifier to a class, so
each topping can have attributes. For example, topping.spicy() returns if a
topping is considered spicy.
"""


class Pizza(object):
    def __init__(self, name=None, sauce='tomato', cheese='mozzarella', toppings=[]):
        # To-do: use self.name as identifier to automatically determine toppings
        self.name = name 
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings
        
    def __str__(self):
        if self.name is None: self.name = 'Custom'
        _ = "{}:\nSauce: {}\nCheese: {}\nToppings: {}\n".format(self.name,
                                                                self.sauce,
                                                                self.cheese,
                                                                self.toppings)
        return _
        
    def price(self):
        return 10
        