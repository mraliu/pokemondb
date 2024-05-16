import tkinter as tk, sqlite3
from tkinter import ttk
conn = sqlite3.connect("pokemon.db")

def searchdb():
    cur = conn.cursor()
    sql = "SELECT * FROM pokemon"
    res = cur.execute(sql)
    return res

res = searchdb()
heading = []

for field in res.description:
    heading.append(field[0])

heading = tuple(heading)

root = tk.Tk()
root.title("DB window")
root.geometry("800x600")

scrollbarv = tk.Scrollbar(root, orient='vertical')
scrollbarh = tk.Scrollbar(root, orient='horizontal')

searchlbl = tk.Label(root, text="Search ")
searchlbl.place(x = 50, y = 75)

searchentry = tk.Entry(root)
searchentry.place(x = 100, y = 75)

searchbtn = tk.Button(root, text="Enter")
searchbtn.place(x = 230, y = 75,width = 80, height = 20)

treeview = ttk.Treeview(columns=heading[1:])

for idx, head in enumerate(heading):
    if idx==0:
        treeview.column("#0", anchor=tk.CENTER, stretch=tk.NO, width=100)
        treeview.heading("#0", text=head)
    else:
        treeview.column(head, anchor=tk.CENTER, stretch=tk.NO, width=100)
        treeview.heading(head, text=head)

for record in res.fetchall():
    treeview.insert("", tk.END, text=record[0], values=record[1:])

treeview.place(x=50,y=125, width=700, height=300)

scrollbarv.place(x=759, y=125, height=300) 
scrollbarh.place(x=50, y=425, width=700)

scrollbarv.config(command = treeview.yview)
scrollbarh.config(command = treeview.xview)





root.mainloop()