import tkinter as tk
import socket
import sys


def connect():

    host = domain_entry_1.get()
    port = int(domain_entry_2.get())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
        result_label.config(text = "Connected to %s on port %d " %(host,port))
    except socket.error as e:
        result_label.config(text = "Can't connect to this connection ,error: %s" % e)
        sys.exit(1)



    




# membuat jendela utama
root = tk.Tk()
root.title('Convert Integer')

# Menambahkan perintah untuk mengatur ukuran jendela
root.geometry('400x300')


domain_label = tk.Label(root, text='Ghaida Fasya Yuthika Afifah \n 714220031 \n D4 TI 2B')
domain_label.pack(pady=10)



# Label dan input domain
domain_label_1 = tk.Label(root, text='Masukan host / web:')
domain_label_1.pack(pady=10)
domain_entry_1 = tk.Entry(root)
domain_entry_1.pack()

domain_label_2 = tk.Label(root, text='Masukan port:')
domain_label_2.pack(pady=10)
domain_entry_2 = tk.Entry(root)
domain_entry_2.pack()


# Button untuk melakukan proses
lookup_button = tk.Button(root, text='Connect', command=connect)
lookup_button.pack(pady=10)

# Label untuk hasil
result_label = tk.Label(root, text='', wraplength=300)
result_label.pack()

root.mainloop()