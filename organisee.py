import shutil
import tkinter as tk
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Label


# from PIL import Image, ImageTk


def organize_files_by_extension(dir_path, new_dir_path):
    # Iterate over all the items in the directory
    for filename in os.listdir(dir_path):
        # Full path of the item
        full_path = os.path.join(dir_path, filename)

        # Check if the item is a file
        if os.path.isfile(full_path):
            # Get the file extension
            extension = os.path.splitext(filename)[1]

            # The directory/folder name will be the file extension
            # If there's no extension, use a default folder name
            folder_name = extension.strip('.') if extension else 'no_extension'

            # Create a new directory in the chosen location if it doesn't exist
            new_folder_path = os.path.join(new_dir_path, folder_name)
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)

            # Check if the file already exists in the new directory
            if os.path.exists(os.path.join(new_folder_path, filename)):
                # If the file exists, append a number to the filename to make it unique
                base, ext = os.path.splitext(filename)
                i = 1
                while os.path.exists(os.path.join(new_folder_path, f"{base}_{i}{ext}")):
                    i += 1
                filename = f"{base}_{i}{ext}"

            # Move the file to the new directory
            shutil.move(full_path, os.path.join(new_folder_path, filename))


def browse_directory():
    # Open the file dialog to choose a directory
    dir_path = filedialog.askdirectory(title="Select the directory to organize")

    # Check if a directory was chosen
    if not dir_path:
        # If not, return immediately
        return

    # Ask the user if they want to use a new directory
    use_new_dir = messagebox.askyesno("Question", "Do you want to organize the files into a new directory?")

    if use_new_dir:
        # Let the user choose the new directory
        new_dir_path = filedialog.askdirectory(title="Select the new directory")
    else:
        # Use the original directory
        new_dir_path = dir_path

    # Organize the files in the chosen directory
    organize_files_by_extension(dir_path, new_dir_path)

    # Close the window after the task is completed
    root.destroy()



# Create the main window
root = tk.Tk()
style = ttk.Style()

root.iconbitmap('4560004.ico')

image1 = tk.PhotoImage(file='organise.png')
w = image1.width()
h = image1.height()
root.geometry("%dx%d+0+0" % (2*w/3, h/2))

# Set the title
root.title('Organise')

# Make the window resizable
root.resizable(True, True)

# Create a label with custom font and background color
label = tk.Label(root, image=image1)
label.pack()

# # Create a label with the text 'Let's Organise'
# organize_label = tk.Label(root, text="Let's Organise", font=('Helvetica',  20), bg='white')
# organize_label.place(relx=0.005, rely=0.05)  # Adjust the position as needed

# Create a button that will open the file dialog when clicked
style.configure('TButton', font=('Helvetica', 20))
browse_button = ttk.Button(root, text="Browse", command=browse_directory, style='TButton')
browse_button.place(relx=0.5, rely=0.65, anchor='center')

# Start the Tkinter event loop
root.mainloop()
