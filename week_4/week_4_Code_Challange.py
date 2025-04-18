def process_file():
    try:
        # Step 1: Read input.txt
        with open("input.txt", "r") as file:
            content = file.read()

        # Step 2: Count the number of words
        word_count = len(content.split())

        # Step 3: Convert all text to uppercase
        content_upper = content.upper()

        # Step 4: Prepare final output
        final_output = content_upper + f"\n\nWord Count: {word_count}"

        # Step 5: Write to output.txt
        with open("output.txt", "w") as output_file:
            output_file.write(final_output)

        # Step 6: Success message
        print("✅ The file 'output.txt' was created successfully with processed content!")

    except FileNotFoundError:
        print("❌ Error: 'input.txt' was not found.")
    except IOError:
        print("❌ Error reading or writing files.")

# Run the function
process_file()
