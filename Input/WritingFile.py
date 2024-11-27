with open('user_data.txt', 'w') as file:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    file.write(f"Name: {name}, Age: {age}")
    print("Data saved to user_data.txt.")
