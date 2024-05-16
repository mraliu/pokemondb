import tkinter as tk, sqlite3
from tkinter import ttk
conn = sqlite3.connect("pokemon.db")

cur = conn.cursor()
sql = "SELECT * FROM pokemon"
res = cur.execute(sql)

heading = []

for field in res.description:
    heading.append(field[0])

heading = tuple(heading)

root = tk.Tk()
root.title("DB window")
root.geometry("800x600")

scrollbarv = tk.Scrollbar(root, orient='vertical')
scrollbarh = tk.Scrollbar(root, orient='horizontal')

treeview = ttk.Treeview(columns=heading[1:])

for idx, head in enumerate(heading):
    if idx==0:
        treeview.column("#0", anchor=tk.CENTER, stretch=tk.NO, width=100)
        treeview.heading("#0", text=head)
    else:
        treeview.column(head, anchor=tk.CENTER, stretch=tk.NO, width=100)
        treeview.heading(head, text=head)


# # treeview.insert("", tk.END, text="#", values=('Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary'))

treeview.place(x=50,y=125, width=700)

scrollbarv.place(x=759, y=125, height=250) 
scrollbarh.place(x=50, y=375, width=700)

scrollbarv.config(command = treeview.yview)
scrollbarh.config(command = treeview.xview)





root.mainloop()