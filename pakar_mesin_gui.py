import tkinter as tk
from tkinter import ttk
from pyswip import Prolog
from tkinter import messagebox

# Inisialisasi Prolog
prolog = Prolog()
prolog.consult("pakar_mesin_gui.pl")

kerusakan = list()
gejala = dict()
index_kerusakan = 0
index_gejala = 0
current_kerusakan = ""
current_gejala = ""

def mulai_diagnosa():
    global kerusakan, gejala, index_kerusakan, index_gejala

    # Bersihkan database Prolog
    prolog.retractall("gejala_pos(_)")
    prolog.retractall("gejala_neg(_)")

    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)

    # Mendapatkan daftar kerusakan dan gejala
    kerusakan = [p["X"].decode() for p in list(prolog.query("kerusakan(X)"))]
    for p in kerusakan:
        gejala[p] = [g["X"] for g in list(prolog.query(f'gejala(X, "{p}")'))]

    index_kerusakan = 0
    index_gejala = -1

    pertanyaan_selanjutnya()

def pertanyaan_selanjutnya(ganti_kerusakan=False):
    global current_kerusakan, current_gejala, index_kerusakan, index_gejala

    # Atur index kerusakan
    if ganti_kerusakan:
        index_kerusakan += 1
        index_gejala = -1

    # Apabila daftar kerusakan sudah habis berarti tidak terdeteksi kerusakan
    if index_kerusakan >= len(kerusakan):
        hasil_diagnosa()
        return
    current_kerusakan = kerusakan[index_kerusakan]

    # Atur index gejala
    index_gejala += 1

    # Apabila semua gejala dari kerusakan habis, berarti terdeteksi kerusakan tsb
    if index_gejala >= len(gejala[current_kerusakan]):
        hasil_diagnosa(current_kerusakan)
        return
    current_gejala = gejala[current_kerusakan][index_gejala]

    # Cek status gejala di database prolog
    if list(prolog.query(f"gejala_pos({current_gejala})")):
        pertanyaan_selanjutnya()
        return
    elif list(prolog.query(f"gejala_neg({current_gejala})")):
        pertanyaan_selanjutnya(ganti_kerusakan=True)
        return

    # Mendapatkan pertanyaan baru
    pertanyaan = list(prolog.query(f"pertanyaan({current_gejala}, Y)"))[0]["Y"].decode()
    
    # Set pertanyaan ke kotak pertanyaan    
    tampilkan_pertanyaan(pertanyaan)

def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.configure(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.configure(state=tk.DISABLED)

def jawaban(jwb):
    if jwb:
        prolog.assertz(f"gejala_pos({current_gejala})")
        pertanyaan_selanjutnya()
    else:
        prolog.assertz(f"gejala_neg({current_gejala})")
        pertanyaan_selanjutnya(ganti_kerusakan=True)

def hasil_diagnosa(kerusakan=""):
    if kerusakan:
        messagebox.showinfo("Hasil Diagnosa", f"Anda terdeteksi {kerusakan}.")
    else:
        messagebox.showinfo("Hasil Diagnosa", "Tidak terdeteksi kerusakan.")

    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)

# Inisialisasi window utama
root = tk.Tk()
root.title("Sistem Pakar Identifikasi Kerusakan Mesin Ekskavator")

# Inisialisasi frame utama
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Membuat widget yang diperlukan
ttk.Label(mainframe, text="Aplikasi Identifikasi Kerusakan Mesin Ekskavator", font=("Arial", 16)).grid(column=0, row=0, columnspan=3)

ttk.Label(mainframe, text="Kolom Pertanyaan:").grid(column=0, row=1)

kotak_pertanyaan = tk.Text(mainframe, height=4, width=40, state=tk.DISABLED)

kotak_pertanyaan.grid(column=0, row=2, columnspan=3)

no_btn = ttk.Button(mainframe, text="Tidak", state=tk.DISABLED, command=lambda: jawaban(False))

no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))

yes_btn = ttk.Button(mainframe, text="Ya", state=tk.DISABLED, command=lambda: jawaban(True))

yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))

start_btn = ttk.Button(mainframe, text="Mulai Diagnosa", command=mulai_diagnosa)

start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

# Tambah padding ke setiap widget
for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# Menjalankan GUI
root.mainloop()