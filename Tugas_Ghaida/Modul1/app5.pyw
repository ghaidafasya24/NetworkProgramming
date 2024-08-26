import tkinter as tk
import socket
from binascii import hexlify

def convert_integer():
    data = int(domain_entry.get())

    try:
        #32bit
        result_label.config(text = f'Original : {data} ==> Long Host Byte Order : {socket.ntohl(data)}, Network Byte Order : {socket.htonl(data)}')
        #16bit
        result_label_1.config(text = f'Original : {data} ==> Short Host Byte Order : {socket.ntohs(data)}, Network Byte Order : {socket.ntohs(data)}')
    except ValueError:
        result_label.config(text = f'Tidak dapat menemukan data {data} error {ValueError}')
    result_label.config(text=result_text)
    
    
 
 
    
# membuat jendela utama
root = tk.Tk()
root.title('Convert IP Address')

# Menambahkan perintah untuk mengatur ukuran jendela
root.geometry('400x300')

result_label = tk.Label(root, text='Ghaida Fasya Yuthika Afifah \n 714220031 \n D4 TI 2B')
result_label.pack(pady=10)

# Label dan input domain
domain_label_1 = tk.Label(root, text='Masukan Data Angka:')
domain_label_1.pack(pady=10)
domain_entry = tk.Entry(root)
domain_entry.pack()

# Button untuk melakukan nslookup
lookup_button = tk.Button(root, text='Convert', command=convert_integer)
lookup_button.pack(pady=10)

# Label untuk hasil
result_label = tk.Label(root, text='', wraplength=300)
result_label.pack()

result_label_1 = tk.Label(root, text='', wraplength=300)
result_label_1.pack()

root.mainloop()