import pizza  # Importing an entire module
import pizza as pz  # Importing an entire module with an alias name

from pizza import make_pizza  # Importing specific functions
from pizza import make_pizza as mp  # Importing specific functions with alias name

# from pizza import *  # Importing all functions in a module

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

pz.make_pizza(16, "pepperoni")
pz.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

mp(16, "pepperoni")
mp(12, "mushrooms", "green peppers", "extra cheese")
