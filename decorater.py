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