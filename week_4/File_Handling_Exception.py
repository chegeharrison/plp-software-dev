def modify_file_content(content):
    # Example modification: convert to uppercase
    return content.upper()

def read_and_write_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content
        modified_content = modify_file_content(content)

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"✅ Modified content written to '{new_filename}' successfully!")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"❌ Error: Could not read or write to the file '{filename}'.")

# Run the function
read_and_write_file()
