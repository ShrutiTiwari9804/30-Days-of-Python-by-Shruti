"""
closures.py

Topics Covered

1. Closures
2. Nested Functions
3. Returning Functions

"""

def multiplier(x):

    """
    Outer Function
    """

    def multiply(number):
        return number * x

    return multiply


def greeting (message):

    def display(name):
        print(message, name)

    return display

def run_closure_demo():

    print("\n------------ Closure Demo -------------\n")

    double = multiplier(2)

    triple = multiplier(3)

    print("Double of 20 =", double(20))

    print("Triple of 20 =", triple(20))

    print()

    hello = greeting("Hello")

    hello("Shruti")
