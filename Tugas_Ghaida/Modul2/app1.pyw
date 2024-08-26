import tkinter as tk
import socket

def test_socket_timeout():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result_label.config(text = "Default socket timeout: %s" %s.gettimeout())
        s.settimeout(100)
        result_label.config(text = "Current socket timeout: %s" %s.gettimeout())
    except socket.gaierror:
        result_label.config(text = f'Error...')

# membuat jendela utama
root = tk.Tk()
root.title('Test Socket Timeout')

# Menambahkan perintah untuk mengatur ukuran jendela
root.geometry('400x200')

domain_label = tk.Label(root, text='Ghaida Fasya Yuthika Afifah \n 714220031 \n D4 TI 2B')
domain_label.pack(pady=10)

# Label dan input domain
domain_label_1 = tk.Label(root, text='Klik untuk mengecek socket timeout')
domain_label_1.pack(pady=10)


# Label untuk melakukan proses
lookup_button = tk.Button(root, text='test', command=test_socket_timeout)
lookup_button.pack(pady=10)

# Label untuk hasil
result_label = tk.Label(root, text='', wraplength=300)
result_label.pack()

root.mainloop()
