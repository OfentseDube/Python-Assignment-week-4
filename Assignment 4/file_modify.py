import os

def modify_and_write_file(input_filename, output_filename):
    """
    Reads a file, modifies its content (adds line numbers), and writes the modified content to a new file.

    Args:
        input_filename (str): The name of the input file.
        output_filename (str): The name of the output file.
    """
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        modified_lines = []
        for i, line in enumerate(lines):
            modified_lines.append(f"{i + 1}: {line}")  # Add line numbers

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"File '{input_filename}' modified and written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read or write files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Gets filename input from user and calls the file modification function.
    """
    input_filename = input("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")

    # Check if the input file exists before attempting to process it.
    if not os.path.exists(input_filename):
        print(f"Error: File '{input_filename}' does not exist.")
        return #exit the function, preventing further errors.

    modify_and_write_file(input_filename, output_filename)

# Create example input files
def create_example_files():
    """Creates two example files for testing."""
    with open("file1.txt", "w") as f1:
        f1.write("This is line 1.\nThis is line 2.\nThis is line 3.")

    with open("file2.txt", "w") as f2:
        f2.write("Hello, world!\nAnother line here.")

create_example_files() #create the example files before the main function runs.

if __name__ == "__main__":
    main()