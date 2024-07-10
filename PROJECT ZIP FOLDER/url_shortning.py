import tkinter as tk
from tkinter import messagebox
import pyshorteners
import pyperclip

def shorten_url():
    url = url_entry.get()
    if url:
        try:
            shortener = pyshorteners.Shortener()
            shortened_url = shortener.tinyurl.short(url)
            shortened_url_entry.delete(0, tk.END)  # Clear previous content
            shortened_url_entry.insert(0, shortened_url)  # Insert shortened URL
            copy_button.config(state=tk.NORMAL)  # Enable copy button
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter a URL")

def copy_url():
    shortened_url = shortened_url_entry.get()
    if shortened_url:
        pyperclip.copy(shortened_url)
        messagebox.showinfo("Copied", "Shortened URL copied to clipboard")
    else:
        messagebox.showwarning("No URL", "There is no URL to copy")

# Create the main tkinter window
root = tk.Tk()
root.title("URL Shortener")

# Create a label and entry for the URL input
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create a button to shorten the URL
shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)

# Create an entry to display the shortened URL
shortened_url_entry = tk.Entry(root, width=50)
shortened_url_entry.pack(pady=10, side=tk.LEFT)

# Create a button to copy the shortened URL
copy_button = tk.Button(root, text="Copy", command=copy_url, state=tk.DISABLED)
copy_button.pack(pady=10, padx=(5, 10), side=tk.LEFT)

# Run the tkinter main loop
root.mainloop()
