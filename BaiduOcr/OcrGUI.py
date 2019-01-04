import tkinter as tk

class Window:
    def __init__(self,title):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry('300x200')

    # ---Label---
    def addLabel(self,name,text,column,row):
        name = tk.Label(text=text)
        name.grid(column=column, row=row)

    # ---Entries---
    def addEntry(self,name,column,row):
        name = tk.Entry()
        name.grid(column=column, row=row)
        return name

    # ---Button---
    def addButton(self,name,text,column,row,function):
        name = tk.Button(text=text, command=function)
        name.grid(column=column, row=row)

# height,width,, , width=width
    # This creates the text field
    def addTextField(self,name,row,text):
        name = tk.Text(master=self.window)
        name.grid(row=row,columnspan=5)

        name.insert(tk.END, text)

    def run(self):
        self.window.mainloop()




