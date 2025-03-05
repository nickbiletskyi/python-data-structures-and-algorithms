


def find_factorial(n):
    if n < 2:
        return n
    return n * find_factorial(n-1)



print(find_factorial(3))