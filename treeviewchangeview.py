import tkinter as tk, sqlite3
from tkinter import ttk
from tkinter import messagebox
conn = sqlite3.connect("pokemon.db")

def getfieldheadings():
    cur = conn.cursor()
    sql = 'SELECT * FROM pokemon'
    headings = cur.execute(sql)
    return headings

def OnDoubleClick(event):
    try:
        # Get the Id of the first selected item.
        item = treeview.selection()[0]
        print(treeview.item(treeview.focus()))
    except IndexError:
        # If the tuple is empty, there is no selected item.
        messagebox.showwarning(message="No Pokemon selected.", title="No selection")
    else:
        # Get and display the text of the selected item.
        text = treeview.item(treeview.focus())['values']
        messagebox.showinfo(message=text, title="Pokemon")

def searchdb(ptype):
    cur = conn.cursor()
    sql = f'SELECT * FROM pokemon WHERE "Type 1" = "{ptype}"'
    res = cur.execute(sql)
    # Clear the treeview
    for item in treeview.get_children():
      treeview.delete(item)
    # Loop through db and add to treeview
    for record in res.fetchall():
        treeview.insert("", tk.END, text=record[0], values=record[1:])
    treeview.bind("<Double-1>", OnDoubleClick)



headings = getfieldheadings()
heading = []

for field in headings.description:
    heading.append(field[0])

heading = tuple(heading)

root = tk.Tk()
root.title("DB window")
root.geometry("800x600")

scrollbarv = tk.Scrollbar(root, orient='vertical')
scrollbarh = tk.Scrollbar(root, orient='horizontal')

grassbtn = tk.Button(root, text="Grass", command=lambda x="Grass":searchdb(x), bg="Green")
grassbtn.place(x = 50, y = 75, width = 100, height = 20)

firebtn = tk.Button(root, text="Fire", command=lambda x="Fire":searchdb(x), bg="Red")
firebtn.place(x = 150, y = 75, width = 100, height = 20)

waterbtn = tk.Button(root, text="Water", command=lambda x="Water":searchdb(x), bg="Aqua")
waterbtn.place(x = 250, y = 75, width = 100, height = 20)

bugbtn = tk.Button(root, text="Bug", command=lambda x="Bug":searchdb(x), bg="Brown")
bugbtn.place(x = 350, y = 75, width = 100, height = 20)

treeview = ttk.Treeview(columns=heading[1:])

for idx, head in enumerate(heading):
    if idx==0:
        treeview.column("#0", anchor=tk.CENTER, stretch=tk.NO, width=100)
        treeview.heading("#0", text=head)
    else:
        treeview.column(head, anchor=tk.CENTER, stretch=tk.NO, width=100)
        treeview.heading(head, text=head)

treeview.place(x=50,y=125, width=700, height=150)

scrollbarv.place(x=759, y=125, height=150) 
scrollbarh.place(x=50, y=275, width=700)

scrollbarv.config(command = treeview.yview)
scrollbarh.config(command = treeview.xview)





root.mainloop()