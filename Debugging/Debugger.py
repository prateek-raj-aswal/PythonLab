import pdb

def divide(a, b): # Set a breakpoint here
    return a / b

print(divide(10, 2))
pdb.set_trace()
print(divide(10, 0))  # Intentional error
