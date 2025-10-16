def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b  # ✅ Swap simultaneously
    return a

print(fibonacci(5))  # Output: 5
