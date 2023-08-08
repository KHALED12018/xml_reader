import re
import tkinter as tk
from tkinter import filedialog

def open_xml_file():
    file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
    if file_path:
        with open(file_path, 'r') as file:
            xml_content = file.read()
            text_elements = re.findall(r'>[^<]+<', xml_content)
            extracted_text = "\n".join([text_element[1:-1] for text_element in text_elements])
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, extracted_text)
            result_text.config(state=tk.DISABLED)
            scrollbar.set(0.0, 0.0)
            separator_label.config(text="------------------")

# Set up the GUI
root = tk.Tk()
root.title("XML Text Extractor")

open_button = tk.Button(root, text="Open XML File", command=open_xml_file)
open_button.pack()

separator_label = tk.Label(root, text="------------------")
separator_label.pack()

result_text = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)
result_text.pack()

scrollbar = tk.Scrollbar(root, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
