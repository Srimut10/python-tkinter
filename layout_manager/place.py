import tkinter as tk

root = tk.Tk()
root.title("Kalkulator")

# Display
entdisplay = tk.Entry(root, width=20, justify="right")
entdisplay.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Fungsi tombol angka/operator
def klik(nilai):
    entdisplay.insert(tk.END, nilai)

# Fungsi hitung
def hitung():
    try:
        hasil = eval(entdisplay.get())
        entdisplay.delete(0, tk.END)
        entdisplay.insert(tk.END, str(hasil))
    except:
        entdisplay.delete(0, tk.END)
        entdisplay.insert(tk.END, "Error")

# Fungsi hapus
def hapus():
    entdisplay.delete(0, tk.END)

# Tombol angka dan operator
btn7 = tk.Button(root, text="7", width=5, command=lambda: klik("7"))
btn8 = tk.Button(root, text="8", width=5, command=lambda: klik("8"))
btn9 = tk.Button(root, text="9", width=5, command=lambda: klik("9"))
btnbagi = tk.Button(root, text="/", width=5, command=lambda: klik("/"))

btn4 = tk.Button(root, text="4", width=5, command=lambda: klik("4"))
btn5 = tk.Button(root, text="5", width=5, command=lambda: klik("5"))
btn6 = tk.Button(root, text="6", width=5, command=lambda: klik("6"))
btnkali = tk.Button(root, text="*", width=5, command=lambda: klik("*"))

btn1 = tk.Button(root, text="1", width=5, command=lambda: klik("1"))
btn2 = tk.Button(root, text="2", width=5, command=lambda: klik("2"))
btn3 = tk.Button(root, text="3", width=5, command=lambda: klik("3"))
btnkurang = tk.Button(root, text="-", width=5, command=lambda: klik("-"))

btn0 = tk.Button(root, text="0", width=5, command=lambda: klik("0"))
btntitik = tk.Button(root, text=".", width=5, command=lambda: klik("."))
btnhitung = tk.Button(root, text="=", width=5, command=hitung)
btntambah = tk.Button(root, text="+", width=5, command=lambda: klik("+"))

# Layout tombol dengan grid
btn7.grid(row=1, column=0, padx=2, pady=2)
btn8.grid(row=1, column=1, padx=2, pady=2)
btn9.grid(row=1, column=2, padx=2, pady=2)
btnbagi.grid(row=1, column=3, padx=2, pady=2)

btn4.grid(row=2, column=0, padx=2, pady=2)
btn5.grid(row=2, column=1, padx=2, pady=2)
btn6.grid(row=2, column=2, padx=2, pady=2)
btnkali.grid(row=2, column=3, padx=2, pady=2)

btn1.grid(row=3, column=0, padx=2, pady=2)
btn2.grid(row=3, column=1, padx=2, pady=2)
btn3.grid(row=3, column=2, padx=2, pady=2)
btnkurang.grid(row=3, column=3, padx=2, pady=2)

btn0.grid(row=4, column=0, padx=2, pady=2)
btntitik.grid(row=4, column=1, padx=2, pady=2)
btnhitung.grid(row=4, column=2, padx=2, pady=2)
btntambah.grid(row=4, column=3, padx=2, pady=2)

root.mainloop()
