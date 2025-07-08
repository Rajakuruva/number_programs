# Print Fibonacci series up to n terms.

def fibonacci_series(n):
    f, s = 0, 1
    result = []
    if n == 1:
        return [f]
    elif n == 2:
        return [f, s]
    
    result = [f, s]
    for _ in range(n - 2):
        t = f + s
        result.append(t)
        f, s = s, t
    return result
