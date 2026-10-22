import tkinter as tk

root = tk.Tk()
root.title("Kalkulator")

# Display
entdisplay = tk.Entry(root, width=24, justify="right", font=("Arial", 16))
entdisplay.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

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

# Fungsi hapus semua
def hapus():
    entdisplay.delete(0, tk.END)

# Fungsi hapus satu karakter
def backspace():
    isi = entdisplay.get()
    entdisplay.delete(0, tk.END)
    entdisplay.insert(tk.END, isi[:-1])

# Warna
warna_angka = {"bg": "white", "fg": "black"}
warna_operator = {"bg": "#4DA6FF", "fg": "white"}
ukuran = {"width": 5, "height": 2, "font": ("Arial", 12)}

# Tombol baris 1
btnC = tk.Button(root, text="C", **ukuran, bg="#FF4D4D", fg="white", command=hapus)
btnback = tk.Button(root, text="⌫", **ukuran, bg="#FF4D4D", fg="white", command=backspace)
btn7 = tk.Button(root, text="7", **ukuran, **warna_angka, command=lambda: klik("7"))
btn8 = tk.Button(root, text="8", **ukuran, **warna_angka, command=lambda: klik("8"))
btn9 = tk.Button(root, text="9", **ukuran, **warna_angka, command=lambda: klik("9"))
btnbagi = tk.Button(root, text="/", **ukuran, **warna_operator, command=lambda: klik("/"))

# Tombol baris 2
btn4 = tk.Button(root, text="4", **ukuran, **warna_angka, command=lambda: klik("4"))
btn5 = tk.Button(root, text="5", **ukuran, **warna_angka, command=lambda: klik("5"))
btn6 = tk.Button(root, text="6", **ukuran, **warna_angka, command=lambda: klik("6"))
btnkali = tk.Button(root, text="*", **ukuran, **warna_operator, command=lambda: klik("*"))

# Tombol baris 3
btn1 = tk.Button(root, text="1", **ukuran, **warna_angka, command=lambda: klik("1"))
btn2 = tk.Button(root, text="2", **ukuran, **warna_angka, command=lambda: klik("2"))
btn3 = tk.Button(root, text="3", **ukuran, **warna_angka, command=lambda: klik("3"))
btnkurang = tk.Button(root, text="-", **ukuran, **warna_operator, command=lambda: klik("-"))

# Tombol baris 4
btn0 = tk.Button(root, text="0", **ukuran, **warna_angka, command=lambda: klik("0"))
btntitik = tk.Button(root, text=".", **ukuran, **warna_angka, command=lambda: klik("."))
btnhitung = tk.Button(root, text="=", **ukuran, **warna_operator, command=hitung)
btntambah = tk.Button(root, text="+", **ukuran, **warna_operator, command=lambda: klik("+"))

# Layout grid
btnC.grid(row=1, column=0, padx=3, pady=3)
btnback.grid(row=1, column=1, padx=3, pady=3)
btn7.grid(row=2, column=0, padx=3, pady=3)
btn8.grid(row=2, column=1, padx=3, pady=3)
btn9.grid(row=2, column=2, padx=3, pady=3)
btnbagi.grid(row=2, column=3, padx=3, pady=3)

btn4.grid(row=3, column=0, padx=3, pady=3)
btn5.grid(row=3, column=1, padx=3, pady=3)
btn6.grid(row=3, column=2, padx=3, pady=3)
btnkali.grid(row=3, column=3, padx=3, pady=3)

btn1.grid(row=4, column=0, padx=3, pady=3)
btn2.grid(row=4, column=1, padx=3, pady=3)
btn3.grid(row=4, column=2, padx=3, pady=3)
btnkurang.grid(row=4, column=3, padx=3, pady=3)

btn0.grid(row=5, column=0, padx=3, pady=3)
btntitik.grid(row=5, column=1, padx=3, pady=3)
btnhitung.grid(row=5, column=2, padx=3, pady=3)
btntambah.grid(row=5, column=3, padx=3, pady=3)

root.mainloop()
