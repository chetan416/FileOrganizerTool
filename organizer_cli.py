# organizer_cli.py

import os
import shutil
import argparse
from pathlib import Path

def organize_directory(directory_path_str: str):
    """
    Organizes files in a directory by moving them into subdirectories
    named after their file extensions.

    Args:
        directory_path_str (str): The path to the directory to organize.
    """
    # Use pathlib for modern, object-oriented path handling.
    # Path.home() gets the user's home directory (e.g., /Users/yourusername on macOS)
    # The '~' symbol is expanded to the home directory.
    directory_path = Path(directory_path_str).expanduser()

    # Check if the provided path is actually a directory.
    if not directory_path.is_dir():
        print(f"Error: The path '{directory_path}' is not a valid directory.")
        return

    print(f"Scanning directory: {directory_path}\n")

    # Use a set to keep track of extensions found to avoid duplicate messages.
    found_extensions = set()

    # Iterate over every item in the specified directory.
    # .iterdir() is a generator, which is memory-efficient for large directories.
    for item_path in directory_path.iterdir():
        # --- Skip directories and the script itself ---
        if item_path.is_dir():
            continue # Go to the next item
        if item_path.name == __file__: # Don't move the script itself
            continue

        # --- Get file extension ---
        # .suffix gives the extension, e.g., '.txt', '.pdf'
        file_extension = item_path.suffix.lower() # Use lowercase for consistency

        if not file_extension:
            # If the file has no extension, skip it.
            print(f"Skipping '{item_path.name}' (no file extension).")
            continue

        # --- Create destination folder ---
        # We remove the dot from the extension, e.g., '.pdf' -> 'pdf'
        # and create a descriptive folder name.
        destination_folder_name = f"{file_extension[1:].upper()} Files"
        destination_folder_path = directory_path / destination_folder_name

        # Create the folder if it doesn't already exist.
        # exist_ok=True prevents an error if the directory is already there.
        destination_folder_path.mkdir(exist_ok=True)

        # --- Move the file ---
        # Construct the full destination path for the file.
        destination_file_path = destination_folder_path / item_path.name

        try:
            # Use shutil.move to move the file.
            shutil.move(str(item_path), str(destination_file_path))
            if file_extension not in found_extensions:
                print(f"Created folder '{destination_folder_name}' for *{file_extension} files.")
                found_extensions.add(file_extension)

        except Exception as e:
            print(f"Could not move '{item_path.name}'. Error: {e}")

    print("\nOrganization complete!")


# This block allows the script to be run directly.
# We will replace the hardcoded path with command-line arguments in the next step.
if __name__ == "__main__":
    # --- Command-line interface setup ---
    # We use argparse to handle command-line arguments.
    # This allows users to specify the directory they want to organize.
    # 1. Create the parser
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by their extension."
    )

    # 2. Add the arguments
    parser.add_argument(
        "-d", "--directory",  # Short and long forms of the argument
        type=str,             # The input should be treated as a string
        required=True,        # This argument is mandatory
        help="The path to the directory you want to organize." # Help message
    )

    # 3. Parse the arguments from the command line
    args = parser.parse_args()

    # 4. Call our function with the user-provided directory
    # The directory is accessed via 'args.directory'
    organize_directory(args.directory)
