import tkinter as tk

root = tk.Tk()
root.title("pack layout manager")
root.geometry("400x300")

lblname = tk.Label(root, text="Nama:")
entname = tk.Entry(root)

lblemail = tk.Label(root, text="Email:")
entemail = tk.Entry(root)

lblpassword = tk.Label(root, text="Password:")
entpassword = tk.Entry(root)


btnsumit = tk.Button(root, text="Login")


lblname.pack(anchor=tk.W)
entname.pack(anchor=tk.W)

lblemail.pack(anchor=tk.W)
entemail.pack(anchor=tk.W)

lblpassword.pack(anchor=tk.W)
entpassword.pack(anchor=tk.W)

btnsumit.pack(anchor=tk.W)

root.mainloop()