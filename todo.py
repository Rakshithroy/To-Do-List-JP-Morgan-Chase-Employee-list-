import tkinter as tk
from tkinter import messagebox, PhotoImage

class jpmorganChase:
    def __init__(self,root):
        self.root=root
        self.root.title("JP Morgan Chase List Of Employes")
        logo = PhotoImage(file='chase.png')
        self.root.iconphoto(False, logo)
        self.root.configure( bg= "navy blue")
        
        self.entry =tk.Entry(root,width=35)
        self.add_button =tk.Button(root,text="Add Name",command=self.add_task)
        self.list_box =tk.Listbox(root,width=40,height=10)
        self.remove_button =tk.Button(root,text="Remove Name",command=self.remove_task)

        self.entry.grid(row=0,column = 0,padx=10,pady=10)
        self.add_button.grid(row=0,column = 1,padx=10,pady=10)
        self.list_box.grid(row=1,column = 0,padx=10,pady=10,columnspan=2)
        self.remove_button.grid(row=2,column = 0,padx=10,pady=10,columnspan=2)


    def add_task(self):
        pass
    def remove_task(self):
        pass
    def update_task(self):
        pass
window =tk.Tk()
app=jpmorganChase(window)
window.mainloop()