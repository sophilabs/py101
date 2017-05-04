Szdef how_many_fib(n):
    a = 0
    b = 1
    result = 0
    while b < n:
        temp = a
        a = b
        b = temp + b
        result = result + 1
    return result

def say_hello():
    print("Say my name")