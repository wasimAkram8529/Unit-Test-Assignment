def add(a, b):
    return a + b

def div(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b
