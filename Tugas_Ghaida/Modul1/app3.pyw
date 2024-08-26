import tkinter as tk
import socket
from binascii import hexlify

def convert_ip4_address():
    ip_address1 = domain_entry1.get()
    ip_address2 = domain_entry2.get()
    
    result_text = ""

    try:
        for ip_addr in [ip_address1, ip_address2]:
            packed_ip_addr = socket.inet_aton(ip_addr)
            unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
            result_text += f"IP Address: {ip_addr} => Packed: {hexlify(packed_ip_addr)}, Unpacked: {unpacked_ip_addr}\n"
    except (socket.error, OSError):
        result_text += "Error during IP address conversion\n"

    result_label.config(text=result_text)
 
 
    
# membuat jendela utama
root = tk.Tk()
root.title('Convert IP Address')

# Menambahkan perintah untuk mengatur ukuran jendela
root.geometry('400x400')

domain_label = tk.Label(root, text='Ghaida Fasya Y A \n 714220031 \n D4 TI 2B')
domain_label.pack(pady=10)
# Label dan input domain
domain_label1 = tk.Label(root, text='Masukan IP Address 1 :')
domain_label1.pack(pady=10)
domain_entry1 = tk.Entry(root)
domain_entry1.pack()

domain_label2 = tk.Label(root, text='Masukan IP Address 2 :')
domain_label2.pack(pady=10)
domain_entry2 = tk.Entry(root)
domain_entry2.pack()


# Label untuk melakukan nslookup
lookup_button = tk.Button(root, text='Convert', command=convert_ip4_address)
lookup_button.pack(pady=10)

# Label untuk hasil
result_label = tk.Label(root, text='', wraplength=300)
result_label.pack()

root.mainloop()