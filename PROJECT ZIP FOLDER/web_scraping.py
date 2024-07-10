import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

# Function to perform web scraping and save readable content to a file
def scrape_and_save():
    url = url_entry.get()  # Get URL from entry widget
    if not url:
        messagebox.showwarning('Warning', 'Please enter a valid URL')
        return
    
    try:
        # Make a GET request
        r = requests.get(url)
        r.raise_for_status()  # Raise error for bad response status

        # Parse the HTML content
        soup = BeautifulSoup(r.content, 'html.parser')

        # Find all elements and extract readable text content
        readable_content = []

        # Selectively include certain tags for readability
        for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'table']):
            if tag.name == 'table':
                # For tables, extract text from table rows and cells
                table_rows = tag.find_all('tr')
                table_content = []
                for tr in table_rows:
                    row_content = []
                    for td in tr.find_all(['td', 'th']):
                        row_content.append(td.get_text(strip=True))
                    table_content.append('\t'.join(row_content))
                readable_content.append('\n'.join(table_content))
            elif tag.name in ['ul', 'ol']:
                # For lists, extract list items
                list_items = tag.find_all('li')
                list_content = [li.get_text(strip=True) for li in list_items]
                readable_content.append('\n'.join(list_content))
            else:
                # For other tags (paragraphs, headings), extract text
                readable_content.append(tag.get_text(strip=True))

        # Save readable content into a single text file
        output_file = 'output.txt'
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n\n'.join(readable_content))

        messagebox.showinfo('Success', f'Readable content saved to {output_file}')
    
    except requests.exceptions.RequestException as e:
        messagebox.showerror('Error', f'Error fetching URL:\n{str(e)}')

# Create the main application window
root = tk.Tk()
root.title('Web Scraping GUI')

# Create URL input label and entry
url_label = tk.Label(root, text='Enter URL:')
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(padx=20, pady=5)

# Create button to trigger scraping
scrape_button = tk.Button(root, text='Scrape and Save', command=scrape_and_save)
scrape_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
