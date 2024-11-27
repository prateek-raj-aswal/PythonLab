def even_numbers():
    for num in range(0, 20, 2):
        yield num

# Use the generator
gen = even_numbers()
print("First 10 even numbers:")
for value in gen:
    print(value)
