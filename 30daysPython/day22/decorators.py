"""
decorators.py

Topics Covered:
1. Decorators
2. Wrapper Functions
3. *args and **kwrags in decorators
4. Multiple Decorators
5. Function Timing
6. Logging
7. Authentication Decorator

"""

import time
from functools import wraps

# ----------------- TIMER DECORATOR -----------------------#

def timer(func):
    """
    Calculates how long a function takes to execute.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"\nExecution Time: {end-start:.6f} seconds\n")

        return result
    
    return wrapper


#------------------------ LOGGER DECORATOR ----------------------#

def logger(func):
    """
    Prints function name, arguments and return value.
    """
    @wraps (func)
    def wrapper(*args, **kwargs):

        print("=" * 50)
        print("Functions: ", func.__name__)
        print("Arguments : " ,args)
        print("Keyword Arguments: ", kwargs)

        result = func(*args, **kwargs)

        print("Returned: ",result)
        print("=" * 50)

        return result
    
    return wrapper

# ------------------- AUTH DECORATOR ----------------------------#

logged_in = True

def authenticate(func):
    """
    Simulates authentication.
    """

    @wraps(func)
    def wrapper (*args, **kwargs):

        if logged_in:
            print("Login Successful\n")
            return func(*args,**kwargs)
        
        else:
            print("Access Denied!")

    return wrapper


#----------------- MULTIPLE DECORATORS --------------------#

@authenticate
@logger
@timer

def calculate_square(number):

    time.sleep(1)

    return number ** 2


#------------------ ANOTHER EXAMPLE --------------------#

@logger 
@timer

def greet(name):

    time.sleep(0.5)

    return f"welcome {name}"


# ----------- TEST FUNCTION --------------#

def run_decorator_demo():

    print("\n------ Decoartor Demonstration ---------\n")

    calculate_square(10)

    greet("Shruti")

    


