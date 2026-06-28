def fib(limit):
    a = 0
    b = 1
    for i in range(limit):
        yield a
        temp =  a
        a, b = b, temp + b

for _ in fib(10):
    print(_)
    