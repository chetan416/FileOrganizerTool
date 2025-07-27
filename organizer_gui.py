# organizer_gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os # Needed for os.path.expanduser

# Import our core logic function from the other file.
from organizer_cli import organize_directory

class FileOrganizerApp(tk.Tk):
    """
    A simple GUI application for organizing files in a directory.
    """
    def __init__(self):
        super().__init__()

        # --- Window Configuration ---
        self.title("File Organizer")
        self.geometry("500x250")
        self.configure(bg="#2e2e2e")

        # --- State Variable ---
        self.selected_directory = tk.StringVar()

        # --- UI Widgets ---
        self.create_widgets()

    def create_widgets(self):
        """Creates and arranges the widgets in the main window."""
        main_frame = tk.Frame(self, padx=20, pady=20, bg=self["bg"])
        main_frame.pack(expand=True, fill="both")

        title_label = tk.Label(
            main_frame,
            text="Select a Directory to Organize",
            font=("Helvetica", 16, "bold"),
            bg=self["bg"],
            fg="#ffffff"
        )
        title_label.pack(pady=(0, 20))

        dir_frame = tk.Frame(main_frame, bg=self["bg"])
        dir_frame.pack(fill="x", pady=10)

        dir_label = tk.Label(
            dir_frame,
            textvariable=self.selected_directory,
            font=("Helvetica", 12),
            bg="#4a4a4a",
            fg="#d0d0d0",
            borderwidth=2,
            relief="sunken",
            padx=10,
            anchor="w"
        )
        self.selected_directory.set("No directory selected...")
        dir_label.pack(side="left", fill="x", expand=True, ipady=5)

        select_button = tk.Button(
            dir_frame,
            text="Select...",
            font=("Helvetica", 12),
            command=self.select_directory_action,
            bg="#007aff",
            fg="white",
            activebackground="#005ecb",
            activeforeground="white",
            borderwidth=0,
            padx=10
        )
        select_button.pack(side="left", padx=(10, 0))

        self.organize_button = tk.Button(
            main_frame,
            text="Organize Files",
            font=("Helvetica", 14, "bold"),
            command=self.organize_files_action,
            bg="#34c759",
            fg="white",
            activebackground="#2ca349",
            activeforeground="white",
            borderwidth=0,
            pady=8
        )
        self.organize_button.pack(fill="x", pady=(20, 0))

        self.status_label = tk.Label(
            main_frame,
            text="",
            font=("Helvetica", 10, "italic"),
            bg=self["bg"],
            fg="#8e8e93"
        )
        self.status_label.pack(pady=(10, 0))

    def select_directory_action(self):
        """
        Opens a dialog to select a directory. The path is stored in
        self.selected_directory.
        """
        # filedialog.askdirectory() opens the native macOS folder picker.
        # It returns the selected path as a string.
        directory_path = filedialog.askdirectory(
            title="Select a Folder to Organize"
        )
        if directory_path:
            # We store the selected path in our special Tkinter variable.
            # The UI label will update automatically.
            self.selected_directory.set(directory_path)
            self.status_label.config(text="") # Clear status on new selection

    def organize_files_action(self):
        """
        Starts the file organization process in a new thread to keep
        the GUI responsive.
        """
        directory = self.selected_directory.get()

        # --- Input Validation ---
        if not directory or directory == "No directory selected...":
            messagebox.showerror("Error", "Please select a directory first.")
            return

        # --- Start the process in a background thread ---
        # This prevents the GUI from freezing while files are being moved.
        # 'target' is the function to run in the new thread.
        # 'args' is a tuple of arguments to pass to that function.
        thread = threading.Thread(target=self.run_organization_task, args=(directory,))
        thread.start()

    def run_organization_task(self, directory):
        """
        The actual worker function that runs the organization logic and
        updates the UI. This function is executed in the background thread.
        """
        # --- Update UI - Disable button and show status ---
        self.organize_button.config(state="disabled", text="Organizing...")
        self.status_label.config(text=f"Processing {os.path.basename(directory)}...")

        try:
            # --- Call the core logic ---
            organize_directory(directory)

            # --- Update UI - Show success message ---
            self.status_label.config(text="Organization complete!")
            messagebox.showinfo("Success", "Files have been successfully organized.")

        except Exception as e:
            # --- Update UI - Show error message ---
            self.status_label.config(text="An error occurred.")
            messagebox.showerror("Error", f"An error occurred during organization:\n{e}")

        finally:
            # --- Update UI - Re-enable button ---
            # This 'finally' block ensures the button is always re-enabled,
            # even if an error occurs.
            self.organize_button.config(state="normal", text="Organize Files")
            self.selected_directory.set("No directory selected...")


if __name__ == "__main__":
    app = FileOrganizerApp()
    app.mainloop()
