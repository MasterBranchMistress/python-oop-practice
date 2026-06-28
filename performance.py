#Performance Decorator

def performance(func):
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@performance
def long_running_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

long_running_function()