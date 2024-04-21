import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Set the color scheme for the dark theme
BACKGROUND_COLOR      = "#2b2b2b"  # Dark gray
FOREGROUND_COLOR      = "#ffffff"  # White
BUTTON_COLOR          = "#444444"  # Gray
BUTTON_HOVER_COLOR    = "#666666"  # Lighter gray

# Dictionary mapping file extensions to their respective folders
file_extensions = \
{
    "pdf" : "PDFs",
    "png" : "Images",
    "jpg" : "Images",
    "jpeg": "Images",
    "gif" : "Images",
    "avif" : "Images",
    "doc" : "Documents",
    "docx": "Documents",
    "txt" : "Documents",
    "rtf" : "Documents",
    "csv" : "Data",
    "xlsx": "Data",
    "zip" : "Archives",
    "7z"  : "Archives",
    "rar" : "Archives",
    "exe" : "Executables",
    "bin" : "Executables",
    "msi" : "Executables",
    "appinstaller" : "Executables",
    "mp3" : "Music",
    "wav" : "Music",
    "mp4" : "Videos",
    "m4a" : "Videos",
    "avi" : "Videos",
    "flv" : "Videos",
    "wmv" : "Videos",
    "ppt" : "Presentations",
    "pptx": "Presentations",
    "html": "Web",
    "css" : "Web",
    "js"  : "Web",
    "py"  : "Python Files",
    "pyc"  : "Python Files",
    "java": "Java Files",
    "c"   : "C Files",
    "cpp" : "C++ Files",
    "h"   : "Header Files",
    "sh"  : "Shell Scripts",
    "bat" : "Batch Files",
    "psd" : "Photoshop Files",
    "ai"  : "Illustrator Files",
    "svg" : "Vector Graphics",
    "xls" : "Excel Files",
    "json": "JSON Files",
    "xml" : "XML Files",
    "sql" : "SQL Files",
    "db"  : "Database Files",
    "md"  : "Markdown Files",
    "log" : "Log Files",
    "bak" : "Backup Files",
    "conf": "Configuration Files",
    "dll" : "Dynamic Link Libraries",
    "iso" : "ISO Files",
    "ico" : "Icon Files",
    "torrent": "Torrent Files",
    "schematic": "Schematic Files",
    "schem": "Schematic Files",
    "apk": "Apk Files",
    "sql": "SQL Files",
    "drawio": "DrawIO Files",
}

def organize_files():
    # Open a folder selection dialog
    folder_selected = filedialog.askdirectory()
    
    if folder_selected:
        try:
            # Iterate over all files in the selected folder
            for filename in os.listdir(folder_selected):
                # Get the file extension
                _, file_extension = os.path.splitext(filename)
                file_extension = file_extension[1:].lower()  # Remove the leading dot and convert to lowercase
                
                # Check if the file extension is in the dictionary
                if file_extension in file_extensions:
                    # Create the destination folder if it doesn"t exist
                    dest_folder = os.path.join(folder_selected, file_extensions[file_extension])
                    os.makedirs(dest_folder, exist_ok=True)
                    
                    # Move the file to the destination folder
                    src_file = os.path.join(folder_selected, filename)
                    dest_file = os.path.join(dest_folder, filename)
                    shutil.move(src_file, dest_file)
                    
            messagebox.showinfo("Success", "Files organized successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("No Folder Selected", "Please select a folder to organize files.")


# Create the GUI
root = tk.Tk()
root.title("File Organizer")
root.geometry("300x40")
root.iconbitmap("/Programming/File-Organizer/icon.ico")
root.configure(bg=BACKGROUND_COLOR)
root.resizable(False, False)
root.eval("tk::PlaceWindow . center")

# Create a button to trigger the file organization
organize_button = tk.Button \
(
    root,
    text="Choose a Folder to be Organized",
    command=organize_files,
    bg=BUTTON_COLOR,
    fg=FOREGROUND_COLOR,
    activebackground=BUTTON_HOVER_COLOR,
    activeforeground=FOREGROUND_COLOR
)
organize_button.pack(pady=10)

# Start the main event loop
root.mainloop()
