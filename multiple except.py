def read_file(file_name):
    try:
        print(f"Trying to open the file: {file_name}")
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError as e:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Execution of file operation is complete.\n")

# Test cases
read_file("existing_file.txt")  # Replace with a real file name that exists
read_file("non_existing_file.txt")  # Simulates a non-existent file
