def read_file_in_binary(file_path):
    try:
        # Open the file in binary read mode
        with open(file_path, 'rb') as file:
            binary_data = file.read()
            print("File read in binary format successfully.")
            return binary_data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the file path
file_path = 'logo.jpeg'  # Replace with your text file path

# Read the file in binary mode
binary_content = read_file_in_binary(file_path)

# If content is read successfully, print a portion of it
if binary_content:
    print("Binary content (first 100 bytes):")
    print(binary_content[:100])
