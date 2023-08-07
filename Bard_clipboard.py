import tkinter as tk
from tkinter import filedialog
from docx import Document
import pyperclip

def on_add_button_click():
    template = template_text.get("1.0", tk.END).strip()
    if template:
        templates_listbox.insert(tk.END, template)
        template_text.delete("1.0", tk.END)

def on_edit_button_click():
    selection = templates_listbox.curselection()
    if selection:
        index = selection[0]
        template = templates_listbox.get(index)
        template_text.delete("1.0", tk.END)
        template_text.insert(tk.END, template)
        templates_listbox.delete(index)

def on_delete_button_click():
    selection = templates_listbox.curselection()
    if selection:
        index = selection[0]
        templates_listbox.delete(index)

def on_save_button_click():
    templates = list(templates_listbox.get(0, tk.END))
    with open("templates.rtf", "wb") as f:
        for template in templates:
            f.write(template.encode("utf-8"))

def on_copy_button_click():
    selection = templates_listbox.curselection()
    if selection:
        index = selection[0]
        template = templates_listbox.get(index)
        pyperclip.copy(template)

def on_template_click(event):
    selection = templates_listbox.curselection()
    if selection:
        index = selection[0]
        template = templates_listbox.get(index)
        pyperclip.copy(template)

def on_save_as_button_click():
    filename = filedialog.asksaveasfilename(filetypes=[("RTF Files", "*.rtf")])
    if filename:
        templates = list(templates_listbox.get(0, tk.END))
        with open(filename, "wb") as f:
            for template in templates:
                f.write(template.encode("utf-8"))

def on_open_button_click():
    filename = filedialog.askopenfilename(filetypes=[("RTF Files", "*.rtf")])
    if filename:
        with open(filename, "rb") as f:
            templates = f.read().decode("utf-8").split("\n")
            templates_listbox.delete(0, tk.END)
            for template in templates:
                templates_listbox.insert(tk.END, template)

root = tk.Tk()
root.title("My Clipboard Tool")

templates_listbox = tk.Listbox(root, width=40)
templates_listbox.bind("<<ListboxSelect>>", on_template_click)
templates_listbox.pack()

template_text = tk.Text(root, width=40)
template_text.pack()

add_button = tk.Button(root, text="Add", command=on_add_button_click)
add_button.pack()

edit_button = tk.Button(root, text="Edit", command=on_edit_button_click)
edit_button.pack()

delete_button = tk.Button(root, text="Delete", command=on_delete_button_click)
delete_button.pack()

save_button = tk.Button(root, text="Save", command=on_save_button_click)
save_button.pack()

copy_button = tk.Button(root, text="Copy", command=on_copy_button_click)
copy_button.pack()

save_as_button = tk.Button(root, text="Save As", command=on_save_as_button_click)
save_as_button.pack()

open_button = tk.Button(root, text="Open", command=on_open_button_click)
open_button.pack()

root.mainloop()
