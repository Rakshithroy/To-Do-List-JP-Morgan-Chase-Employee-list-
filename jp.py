import tkinter as tk
from tkinter import messagebox, PhotoImage

class JPMorganChase:
    def __init__(self, root):
        self.root = root
        self.root.title("JP Morgan Chase List Of Employees")
        
        
        logo = PhotoImage(file='chase.png')
        self.root.iconphoto(False, logo)

        self.root.configure(bg="navy blue")

       
        self.label_name = tk.Label(root, text="Name:", bg="light blue")
        self.label_name.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        
       
        self.name_entry = tk.Entry(root, width=20)
        self.name_entry.grid(row=1, column=0, padx=5, pady=5, sticky='w')

     
        self.label_position = tk.Label(root, text="Position:", bg="light blue")
        self.label_position.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        
      
        self.position_entry = tk.Entry(root, width=20)
        self.position_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # Buttons
        self.add_button = tk.Button(root, text="Add Employee", command=self.add_task,bg="green")
        self.add_button.grid(row=1, column=2, padx=10, pady=5)
        
        self.update_button = tk.Button(root, text="Update Employee", command=self.update_task)
        self.update_button.grid(row=2, column=2, padx=10, pady=5)
        
        self.list_box = tk.Listbox(root, width=50, height=10)
        self.list_box.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky='we')

        self.remove_button = tk.Button(root, text="Remove Employee",command=self.remove_task,bg="red")
        self.remove_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10, sticky='we')

    def add_task(self):
        name = self.name_entry.get().strip()
        position = self.position_entry.get().strip()
        if name and position:
            employee_info = f"{name} - {position}"
            self.list_box.insert(tk.END, employee_info)
            self.name_entry.delete(0, tk.END)
            self.position_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Add Task", "Please enter both name and position.")

    def remove_task(self):
        try:
            self.list_box.delete(self.list_box.curselection())
        except:
            messagebox.showwarning("Remove Task", "Please select an employee to remove.")

    def update_task(self):
        try:
            index = self.list_box.curselection()[0]
            name = self.name_entry.get().strip()
            position = self.position_entry.get().strip()
            if name and position:
                employee_info = f"{name} - {position}"
                self.list_box.delete(index)
                self.list_box.insert(index, employee_info)
                self.name_entry.delete(0, tk.END)
                self.position_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Update Task", "Please enter both name and position.")
        except:
            messagebox.showwarning("Update Task", "Please select an employee to update.")

window = tk.Tk()
app = JPMorganChase(window)
window.mainloop()
