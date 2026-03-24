"""
Lab Assignment-1
Question: Construct a program that reads a text file and writes its 
contents into a new text file with the same content, but in uppercase.
"""

def convert_to_uppercase(source_filename, destination_filename):
    try:
        # Open source file for reading and destination for writing
        with open(source_filename, 'r') as source_file:
            content = source_file.read()
            
        # Convert content to uppercase
        uppercase_content = content.upper()
        
        with open(destination_filename, 'w') as dest_file:
            dest_file.write(uppercase_content)
            
        print(f"Successfully converted '{source_filename}' to uppercase in '{destination_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{source_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ensure 'sample.txt' exists in your VS Code directory for this to run
    convert_to_uppercase('sample.txt', 'sample_uppercase.txt')
