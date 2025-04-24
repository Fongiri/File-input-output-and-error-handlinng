# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

def modify_and_write_file(input_filename, output_filename, modification_function):
    """
    Reads a file, modifies its content using a function, and writes the result to a new file.

    Args:
        input_filename: Path to the input file.
        output_filename: Path to the output file.
        modification_function: A function that takes a string (file content) as input and returns the modified string.
                            Must return None to signal an error.
    Returns:
        True if successful, False otherwise.  Prints informative error messages.
    """
    try:
        with open(input_filename, 'r') as infile:
            file_content = infile.read()
            modified_content = modification_function(file_content)
            
            if modified_content is None:  # Check for error from modification function
                print(f"Error modifying file content in {input_filename}.")
                return False

            with open(output_filename, 'w') as outfile:
                outfile.write(modified_content)
            return True

    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


# Example modification function (convert to uppercase):
def to_uppercase(text):
    return text.upper()


# Example modification function (replace specific string)
def replace_string(text, old_string, new_string):
    try:
        return text.replace(old_string, new_string)
    except TypeError:  # Handles cases where text is not a string
        print(f"Error: Input text is not a string.")
        return None


# Example usage (File Read & Write Challenge):
if __name__ == "__main__":
    input_file = 'input.txt'  # Replace with your input file
    output_file = 'output.txt' # Replace with your desired output file
    
    # Example to convert to uppercase
    success = modify_and_write_file(input_file, output_file, to_uppercase)
    if success:
        print(f"Successfully wrote modified content to {output_file}")

    #Example to replace a specific string
    success = modify_and_write_file(input_file, output_file + "_replace", lambda txt: replace_string(txt,"old","new"))
    if success:
        print(f"Successfully wrote modified content to {output_file}_replace")