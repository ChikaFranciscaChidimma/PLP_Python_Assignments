def read_and_modify_file():
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Attempt to open and read the file
        with open(input_filename, 'r') as file:
            content = file.read()
            print("✅ File read successfully!")

        # Modify the content (e.g., make it uppercase)
        modified_content = content.upper()

        # Generate output file name
        output_filename = "modified_" + input_filename

        # Write the modified content to a new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
            print(f"✅ Modified content written to '{output_filename}'")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
