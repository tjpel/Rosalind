def fib(n: int, k: int):
    if n == 1:
        return 1
    elif n == 2:
        return k
    elif n <= 4:
        return (fib(n-1, k) + fib(n-2, k))
    
    return (fib(n-1,k) + fib(n-2, k) * k)
        
print(fib(35, 5))