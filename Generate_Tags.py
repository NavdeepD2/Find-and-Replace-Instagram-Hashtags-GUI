# Written by Navdeep Singh
# Email: navdeep.d2@gmail.com
import tkinter as tk
import pyperclip

# Function to perform the Find and Replace operation and copy to clipboard
def replace_and_copy():
    find_text = find_entry.get()
    replace_text = replace_entry.get().replace(" ", "")
    #replace_text = replace_entry.get()
    tags_data = tags_text.get("1.0", "end-1c")  # Get the current text in the tags_text widget
    updated_tags = tags_data.replace(find_text, replace_text)
    pyperclip.copy(updated_tags)  # Copy the updated tags to the clipboard
    tags_text.delete("1.0", "end")  # Clear the tags_text widget
    tags_text.insert("1.0", updated_tags)  # Insert the updated tags

# Create the main application window
root = tk.Tk()
root.title("Find and Replace Tags")

# Create labels for the text boxes
find_label = tk.Label(root, text="Find:")
find_label.pack()

# Text box 1 (Find)
find_entry = tk.Entry(root)
find_entry.pack()

replace_label = tk.Label(root, text="Replace:")
replace_label.pack()

# Text box 2 (Replace)
replace_entry = tk.Entry(root)
replace_entry.pack()

# Create a multi-line text widget
tags_text = tk.Text(root, height=10, width=40)
tags_text.pack()

# Create the "Replace and Copy" button
replace_button = tk.Button(root, text="Replace and Copy", command=replace_and_copy)
replace_button.pack()

# Start the Tkinter main loop
root.mainloop()
