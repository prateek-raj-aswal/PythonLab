def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Use the generator
fib_gen = fibonacci()
print("Fibonacci numbers less than 100:")
for value in fib_gen:
    if value >= 100:
        break
    print(value)
