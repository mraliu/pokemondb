import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("DB window")
root.geometry("800x600")

treeview = ttk.Treeview(columns=("Item 1", "Item 2"))

treeview.heading("#0", text="File")
treeview.heading("Item 1", text="File")
treeview.heading("Item 2", text="File")



treeview.insert("", tk.END, text="Item", values=("A", "B"))

treeview.pack()

root.mainloop()