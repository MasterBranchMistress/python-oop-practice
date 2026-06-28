#Decorators are a very powerful and useful tool in 
# Python since it allows programmers to modify 
# the behavior of function or class. 
# Decorators allow us to wrap another function in 
# order to extend the behavior of the 
# wrapped function, without permanently 
# modifying it.

def myDecorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@myDecorator
def hello(greeting, emoji=":D"):
    print(f"{greeting} {emoji}")

hello("Hello, world!")