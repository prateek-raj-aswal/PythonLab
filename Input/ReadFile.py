try:
    with open('user_data.txt', 'r') as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print("File not found. Please run the write program first.")
