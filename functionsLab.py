# def greet():
#     print("Hello, welcome to Python Lab!")
#
# greet()


# def calculate_area(length, width):
#     area = length * width
#     print(f"The area of the rectangle is: {area}")
#
# calculate_area(5, 10)


# def find_square(number):
#     return number * number
#
# result = find_square(4)
# print(f"The square is: {result}")


# def introduce(name, age=25):
#     print(f"Hi, I am {name} and I am {age} years old.")
#
# introduce("Alice")
# introduce("Bob", 30)

# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x: x * 2, numbers))
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print("Doubled numbers:", doubled)
# print("Even numbers:", evens)


def outer_function():
    def inner_function():
        return "Hello from the inner function!"
    return inner_function()

print(outer_function())
