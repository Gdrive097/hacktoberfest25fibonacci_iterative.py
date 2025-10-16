def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a = b
        b = a + b  # ❌ Incorrect update order
    return a

print(fibonacci(5))  # Expected 5
