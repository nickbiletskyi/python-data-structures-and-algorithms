

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-2) + fib(n-1)


print(fib(4))

cache = {0: 0, 1: 1}
def fib_cache(n):
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib_cache(n-1) + fib_cache(n-2)
    return cache[n]


print(fib_cache(4))


def fib_optimized(n):
    """
    bottom up approach
    time complexity: o(n-1)
    space complexity o(1)
    """
    if n <= 1:
        return n
    prev, current = 0, 1
    for _ in range(2, n+1):
        prev, current = current, prev + current
    return current

print(fib_optimized(4))

    