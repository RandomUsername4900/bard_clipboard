import tkinter as tk
import pickle

def on_import_rtf_button_click():
    filename = filedialog.askopenfilename(filetypes=[("RTF Files", "*.rtf")])
    if filename:
        with open(filename, "rb") as f:
            templates = pickle.load(f)
            templates_listbox.delete(0, tk.END)
            for template in templates:
                templates_listbox.insert(tk.END, template)

def on_save_button_click():
    templates = list(templates_listbox.get(0, tk.END))
    with open("templates.pkl", "wb") as f:
        pickle.dump(templates, f)

root = tk.Tk()
root.title("My Clipboard Tool")

templates_listbox = tk.Listbox(root, width=40)
templates_listbox.bind("<<ListboxSelect>>", on_template_click)
templates_listbox.pack()

template_text = tk.Text(root, width=40, state="normal")
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

save_as_rtf_button = tk.Button(root, text="Save As RTF", command=on_import_rtf_button_click)
save_as_rtf_button.pack()

import_rtf_button = tk.Button(root, text="Import RTF", command=import_rtf_button_click)
import_rtf_button.pack()

root.mainloop()
