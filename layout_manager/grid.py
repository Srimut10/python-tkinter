import tkinter as tk

root = tk.Tk()
root.title("Grid Layout Manager")
root.geometry("400x300")

lblname = tk.Label(root, text="Nama:")
entname = tk.Entry(root)

lblemail = tk.Label(root, text="Email:")
entemail = tk.Entry(root)

lblpassword = tk.Label(root, text="Password:")
entpassword = tk.Entry(root, show="*")

btnsumit = tk.Button(root, text="Login")

lblname.grid(row=0, column=0, sticky=tk.W)
entname.grid(row=0, column=1)

lblemail.grid(row=1, column=0, sticky=tk.W)
entemail.grid(row=1, column=1)

lblpassword.grid(row=2, column=0, sticky=tk.W)
entpassword.grid(row=2, column=1)

btnsumit.grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E)

root.mainloop()