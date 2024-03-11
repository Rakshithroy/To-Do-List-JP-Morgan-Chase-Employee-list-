import tkinter as tk
from tkinter import messagebox, PhotoImage

class jpmorganChase:
    def __init__(self, root):
        self.root = root
        self.root.title("JP Morgan Chase List Of Employees")
        
        # Load the PNG file and set it as the window icon
        logo = PhotoImage(file='chase.png')
        self.root.iconphoto(False, logo)

        self.root.configure(bg="navy blue")
        
        self.entry = tk.Entry(root, width=60)
        self.add_button = tk.Button(root, text="Add Name", command=self.add_task,bg='light blue')
        self.position_entry = tk.Entry(root, width=10)
        self.add_button = tk.Button(root, text="Add positon", command=self.add_position,bg='light blue')
        self.update_button = tk.Button(root, text="Update Name", command=self.update_task)
        self.list_box = tk.Listbox(root, width=100, height=20)
        self.remove_button = tk.Button(root, text="Remove Name", command=self.remove_task,bg='red')

        self.entry.grid(row=0, column=0, padx=5, pady=5)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)
        self.position_entry.grid(row=0, column=2, padx=5, pady=10)
        self.add_button.grid(row=0, column=3, padx=5, pady=10)
        self.update_button.grid(row=1, column=2, padx=5, pady=10) 
        self.list_box.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        self.remove_button.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

    def add_task(self):
        name = self.entry.get().strip()  
        if name: 
            
            self.list_box.insert(tk.END, name)
            
            self.entry.delete(0, tk.END)
    def add_position(self):
        name = self.entry.get().strip()  
        if name: 
            
            self.list_box.insert(tk.END, name)
            
            self.entry.delete(0, tk.END)
        

    def remove_task(self):
        try:
            
            self.list_box.delete(self.list_box.curselection())
        except:
            messagebox.showwarning("Remove Task", "Please select a name to remove.")
        

    def update_task(self):
        try:
            
            index = self.list_box.curselection()[0]
            
            new_name = self.entry.get().strip()
            if new_name:
                
                self.list_box.delete(index)
                self.list_box.insert(index, new_name)
                self.entry.delete(0, tk.END)
        except:
            messagebox.showwarning("Update Task", "Please select a name to update.")

window = tk.Tk()
app = jpmorganChase(window)
window.mainloop()
