import tkinter as tk
import socket

def nslookup():
    domain = domain_entry.get()
    try:
        ip_address = socket.gethostbyname(domain)
        result_label.config(text = f'Nama domain : {domain}\n Alamat IP : {ip_address}')
    except socket.gaierror:
        result_label.config(text = f'Tidak dapat menemukan alamat IP untuk domain {domain}')

# membuat jendela utama
root = tk.Tk()
root.title('NSLookup APP')

# Menambahkan perintah untuk mengatur ukuran jendela
root.geometry('400x200')

# Label dan input domain
domain_label = tk.Label(root, text='Masukan domain:')
domain_label.pack(pady=10)
domain_entry = tk.Entry(root)
domain_entry.pack()


# Label untuk melakukan nslookup
lookup_button = tk.Button(root, text='NSLookUp', command=nslookup)
lookup_button.pack(pady=10)

# Label untuk hasil
result_label = tk.Label(root, text='', wraplength=300)
result_label.pack()

root.mainloop()