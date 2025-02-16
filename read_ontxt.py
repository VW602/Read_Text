import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def search_string_in_file(filename, search_string):
  
    results = []
    
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read all the lines from the file
            lines = file.readlines()
            
            # Loop through each line and search for the string
            for line_number, line in enumerate(lines, start=1):
                if search_string in line:
                    # Add the result as a tuple (line number, line content)
                    results.append((line_number, line.strip()))
                    
        if results:
            return results
        else:
            return "The string was not found in the file."
    
    except FileNotFoundError:
        return "The file was not found."


def upload_file():
    """Allow the user to upload a text file for searching."""
    file_path = filedialog.askopenfilename(
        title="Select a file", filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)


def search():
    """Perform the search operation based on the user input."""
    file_path = entry_file_path.get()
    search_str = entry_search_string.get()

    if not file_path:
        messagebox.showerror("Error", "Please upload a file.")
        return
    if not search_str:
        messagebox.showerror("Error", "Please enter a string to search.")
        return

    # Perform the search
    result = search_string_in_file(file_path, search_str)

    # Display the result
    result_box.delete(1.0, tk.END)  # Clear previous results
    if isinstance(result, list):
        result_text = f"The string '{search_str}' was found on the following lines:\n\n"
        for line_number, line_content in result:
            result_text += f"Line {line_number}: {line_content}\n"
    else:
        result_text = result

    result_box.insert(tk.END, result_text)


# Create the main application window
root = tk.Tk()
root.title("Text Search Tool")
root.geometry("500x400")

# Create and place widgets
lbl_upload = tk.Label(root, text="Upload a text file:")
lbl_upload.pack(pady=5)

entry_file_path = tk.Entry(root, width=50)
entry_file_path.pack(pady=5)

btn_upload = tk.Button(root, text="Browse", command=upload_file)
btn_upload.pack(pady=5)

lbl_search = tk.Label(root, text="Enter the string to search for:")
lbl_search.pack(pady=5)

entry_search_string = tk.Entry(root, width=50)
entry_search_string.pack(pady=5)

btn_search = tk.Button(root, text="Search", command=search)
btn_search.pack(pady=10)

# Create a scrolled text box for the results
result_box = scrolledtext.ScrolledText(root, width=60, height=10, wrap=tk.WORD)
result_box.pack(pady=10)

# Run the main application loop
root.mainloop()
