def read_and_modify_file():
    # Asking the user to enter the filename
    filename = input("Enter the filename to read: ")

    try:
        # Open the file in read mode and read its content
        with open(filename, 'r') as file:
            content = file.read()
        
        # Perform some modification on the content (e.g., converting to uppercase)
        modified_content = content.upper()
        
        # Define a new filename to save the modified content
        new_filename = "modified_" + filename
        
        # Write the modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"Modified content has been written to {new_filename}")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: The file cannot be read. Please check file permissions or file path.")

# Run the function
read_and_modify_file()
