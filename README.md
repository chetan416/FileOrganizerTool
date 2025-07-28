# Python File Organizer for macOS

A simple yet powerful tool to automatically organize files in a directory based on their type. This project includes both a Command-Line Interface (CLI) for quick, scriptable organization and a user-friendly Graphical User Interface (GUI) for ease of use.

## Features
Automatic Sorting: Scans a specified directory and moves files into sub-folders named after their extensions (e.g., .pdf files go into a "PDF Files" folder).

## Dual Interface:

**CLI (organizer_cli.py):** A robust command-line tool perfect for power users, automation, and scripting. Uses argparse for clear and mandatory arguments.

**GUI (organizer_gui.py):** A simple, intuitive graphical interface built with Tkinter. Allows users to select a directory with the native macOS Finder and organize with the click of a button.

**Safe:** The script automatically skips over sub-directories and will not move itself.

**Responsive UI:** The GUI runs the file organization task in a separate thread, ensuring the application remains responsive and doesn't freeze, even when processing large directories.

**No External Dependencies:** Built entirely with Python's standard libraries, so it runs out-of-the-box on any system with Python installed.

## Requirements

**Python 3:** This script is written for Python 3.x. It should be pre-installed on modern macOS systems.

## How to Use

**Clone or Download:** Get the project files and place them in a directory (e.g., ~/Desktop/file_organizer).

**Open Terminal:** Navigate to the project directory in your Terminal.

cd ~/Desktop/file_organizer

**Option A:** Using the GUI (Recommended for most users)

Run the GUI application directly from the terminal:

python3 organizer_gui.py

Click the "Select..." button to open a Finder window.

Choose the directory you wish to organize (e.g., your Downloads folder).

Click the "Organize Files" button to start the process.

A confirmation message will appear when the process is complete.

**Option B:** Using the Command-Line Tool

Run the CLI script, providing the path to the directory you want to organize using the mandatory --directory (or -d) flag.

# Example using the long-form argument
python3 organizer_cli.py --directory ~/Downloads

# Example using the short-form argument
python3 organizer_cli.py -d ~/Desktop/messy_folder

The script will print its progress in the terminal.

Project Structure
file_organizer/
├── organizer_cli.py    # The core logic and command-line interface
├── organizer_gui.py    # The graphical user interface application
└── README.md           # This file

organizer_cli.py: Contains the main organize_directory() function which holds all the file-moving logic. It also uses the argparse library to function as a standalone command-line tool.

organizer_gui.py: Imports the logic from organizer_cli.py and wraps it in a user-friendly Tkinter interface. It handles user input (button clicks, directory selection) and uses threading to keep the UI responsive.

# Future Enhancements

**Smart AI Categorization (Advanced):**

Integrate with AI models (like Google's Gemini or other LLMs) to analyze the content of files.

**Documents:** Use Natural Language Processing (NLP) to classify text files (.pdf, .docx, .txt) into folders like "Invoices," "Resumes," "Project Notes," etc.

**Images:** Use computer vision models to categorize images into folders like "Vacation Photos," "Screenshots," "Receipts," etc.

**Custom Rules:** Allow users to define their own rules in a configuration file (e.g., move both .jpg and .png files to a "Images" folder).

**Logging:** Create a log file that records every file move, providing a history of operations.

**"Dry Run" Mode:** Add an option to simulate the organization process, printing what changes would be made without actually moving any files.

**Undo Functionality:** A more advanced feature to revert the most recent organization task.
