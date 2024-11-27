def square_numbers(numbers):
    for num in numbers:
        yield num ** 2

nums = [1, 2, 3, 4]
for square in square_numbers(nums):
    print(square)
