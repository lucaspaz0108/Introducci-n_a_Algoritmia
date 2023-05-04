def fibonacci(n):
    a = 0
    b = 1
    for n in range(2, n):
        c = a+b
        print(c, end=" ")
        a = b
        b = c
    
    return b

print(fibonacci(25))
