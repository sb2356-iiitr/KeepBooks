"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
from tkinter import messagebox
from backend import *

def get_selected_row(event):    # Bind method
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[2])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])

def view_command():
    # Empty the list box before displaying
    list1.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    for row in view():
        # Display in the list box
        list1.insert(END, row)

def search_command():
    # Empty the list box before displaying
    list1.delete(0, END)
    title = title_text.get()
    author = author_text.get()
    year = year_text.get()
    isbn = isbn_text.get()
    if (not title) and (not author) and (not year) and (not isbn):
        messagebox.showerror("Error", "Please input something!")
    elif len(search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())) == 0:
        messagebox.showerror("Error", "No data available")
    else:
        for row in search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
            # Display in the list box
            list1.insert(END, row)

def insert_command():
    # Add to database
    title = title_text.get()
    author = author_text.get()
    year = year_text.get()
    isbn = isbn_text.get()
    if title == "" or author == "" or year == "" or isbn == "":
        messagebox.showerror("Error", "Please fill all empty fields")
    else:
        insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        messagebox.showinfo("Success", "Book details have been added.")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)

def delete_command():
    if selected_tuple:
        res = messagebox.askyesno('Warning!', 'Do you want to delete this book?') 
        if res:
            delete(selected_tuple[0])
            messagebox.showinfo("Success", "The book has been removed.")
        view_command()

def update_command():
    if selected_tuple:
        res = messagebox.askyesno('Warning!', 'Do you want to update details for this book?') 
        if res:
            update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
            messagebox.showinfo("Success", "The book details have been updated.")
        view_command()
    
window = Tk()

window.wm_title("BookStore")  # Name on Title Bar

def exit_command():
    res = messagebox.askyesno('Warning!', 'Do you want to exit?')
    if res:
        window.destroy()

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Year")
l2.grid(row=1, column=0)

l3 = Label(window, text="Author")
l3.grid(row=0, column=3)

l4 = Label(window, text="ISBN-10")
l4.grid(row=1, column=3)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

year_text = StringVar()
e2 = Entry(window, textvariable=year_text)
e2.grid(row=1, column=1)

author_text = StringVar()
e3 = Entry(window, textvariable=author_text)
e3.grid(row=0, column=4)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=4)

list1 = Listbox(window, height=6, width=70)
list1.grid(row=2, column=0, rowspan=6, columnspan=8)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=8, rowspan=6)

list1.configure(yscrollcommand=sb1.set)  # Adds the scrollbar to the right of box
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=9)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=9)

b3 = Button(window, text="Add Entry", width=12, command=insert_command)
b3.grid(row=4, column=9)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=9)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5  .grid(row=6, column=9)

b6 = Button(window, text="Exit", width=12, command=exit_command)
b6  .grid(row=7, column=9)

window.mainloop()