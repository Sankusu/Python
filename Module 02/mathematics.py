# Module: mathematics.py

# Returns Fibonacci series up to n
def fib(n): 
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# Returns factorial of n
def fact(n):
    if n<1: return 1
    else: return n*fact(n-1)


# Returns square of n
def sq(n):
    return n*n
