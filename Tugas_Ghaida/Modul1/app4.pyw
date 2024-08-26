import tkinter as tk
import socket
from binascii import hexlify

def find_service_name():
    port1 = domain_entry1.get()
    port2 = domain_entry2.get()

    result_text = ""

    try:
        for port in [port1, port2]:
            try:
                result_text += f"Port: {port} => Service Name : {socket.getservbyport(int(port), 'tcp')}\n"
                result_text += f"Port: {53} => Service Name : {socket.getservbyport(53, 'udp')}\n"
            except OSError as e:
                result_text += f"Port: {port} => Service Name: Not found or error - {e}\n"

    except ValueError as ve:
        result_text += f"Invalid port number: {ve}"

    result_label.config(text=result_text) 
 
    
# membuat jendela utama
root = tk.Tk()
root.title('Find Service Port Name')

# Menambahkan perintah untuk mengatur ukuran jendela
root.geometry('400x400')

domain_label = tk.Label(root, text='Ghaida Fasya Yuthika Afifah \n 714220031 \n D4 TI 2B')
domain_label.pack(pady=10)
# Label dan input domain
domain_label1 = tk.Label(root, text='Masukan Port 1 :')
domain_label1.pack(pady=10)
domain_entry1 = tk.Entry(root)
domain_entry1.pack()

domain_label2 = tk.Label(root, text='Masukan Port 2 :')
domain_label2.pack(pady=10)
domain_entry2 = tk.Entry(root)
domain_entry2.pack()


# Label untuk melakukan nslookup
lookup_button = tk.Button(root, text='Find', command=find_service_name)
lookup_button.pack(pady=10)

# Label untuk hasil
result_label = tk.Label(root, text='', wraplength=300)
result_label.pack()

root.mainloop()