import tkinter as tk
import pyperclip

class Template:
    def __init__(self, text):
        self.text = text

class ClipboardTool(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.templates = []
        self.template_list = tk.Listbox(self, width=20)
        self.template_list.pack()
        self.add_template_button = tk.Button(self, text="Add Template", command=self.add_template)
        self.add_template_button.pack()
        self.edit_template_button = tk.Button(self, text="Edit Template", command=self.edit_template)
        self.edit_template_button.pack()
        self.paste_template_button = tk.Button(self, text="Paste Template", command=self.paste_template)
        self.paste_template_button.pack()

        self.new_template_entry = tk.Entry(self)
        self.new_template_entry.pack()
        self.new_template_button = tk.Button(self, text="Save", command=self.add_new_template)
        self.new_template_button.pack()

    def add_template(self):
        new_template = self.new_template_entry.get()
        self.templates.append(Template(new_template))
        self.template_list.insert(tk.END, new_template)

    def edit_template(self):
        index = self.template_list.curselection()[0]
        template = self.templates[index]
        entry = tk.Entry(self, text=template.text)
        entry.pack()
        button = tk.Button(self, text="Save", command=lambda: self.update_template(index, entry.get()))
        button.pack()

    def update_template(self, index, new_template):
        self.templates[index] = Template(new_template)
        self.template_list.delete(index)
        self.template_list.insert(index, new_template)

    def paste_template(self):
        index = self.template_list.curselection()[0]
        template = self.templates[index].text
        pyperclip.copy(template)

    def add_new_template(self):
        new_template = self.new_template_entry.get()
        self.templates.append(Template(new_template))
        self.template_list.insert(tk.END, new_template)

root = tk.Tk()
clipboard_tool = ClipboardTool(root)
clipboard_tool.pack()
root.mainloop()
