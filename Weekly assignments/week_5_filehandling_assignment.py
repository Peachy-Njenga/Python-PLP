# file_handling_assignment.py

# File creation: Writing to "my_file.txt"
def create_file():
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Hello, this is line 1.\n")
            file.write("This is line 2 with a number: 42.\n")
            file.write("Final line in write mode.\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"An error occurred while creating or writing the file: {e}")
    finally:
        print("Finished file creation process.")

# File reading: Reading and displaying contents
def read_file():
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File content:\n")
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        print("Finished file reading process.")

# File appending: Adding more lines to "my_file.txt"
def append_file():
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending line 1.\n")
            file.write("Appending line 2 with a number: 99.\n")
            file.write("Final line in append mode.\n")
        print("Lines appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("Finished file appending process.")

# Error Handling demonstration
def main():
    try:
        create_file()
        read_file()
        append_file()
        read_file()  # Read again after appending
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Script execution complete.")

if __name__ == "__main__":
    main()
