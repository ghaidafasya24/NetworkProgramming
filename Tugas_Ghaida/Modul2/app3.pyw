import tkinter as tk
import socket


def modify_buff_size():

    try:
        SEND_BUF_SIZE = int(domain_entry_1.get())
        RECV_BUF_SIZE = int(domain_entry_2.get())
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        result_label.config(text = "Buffer size [Before]: %d" % bufsize)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

        bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        result_label_1.config(text = "Buffer size [After]: %d" % bufsize)
    except ValueError as ve:
        result_label.config(text = "Error %e" %(ve))




    




# membuat jendela utama
root = tk.Tk()
root.title('Size Buffer')

# Menambahkan perintah untuk mengatur ukuran jendela
root.geometry('400x400')


domain_label = tk.Label(root, text='Ghaida Fasya Yuthika Afifah \n 714220031 \n D4 TI 2B')
domain_label.pack(pady=10)



# Label dan input domain
domain_label_1 = tk.Label(root, text='Masukan nilai Buffer 1 :')
domain_label_1.pack(pady=10)
domain_entry_1 = tk.Entry(root)
domain_entry_1.pack()

domain_label_2 = tk.Label(root, text='Masukan nilai Buffer 2 :')
domain_label_2.pack(pady=10)
domain_entry_2 = tk.Entry(root)
domain_entry_2.pack()


# Button untuk melakukan proses
lookup_button = tk.Button(root, text='modif', command=modify_buff_size)
lookup_button.pack(pady=10)

# Label untuk hasil
result_label = tk.Label(root, text='', wraplength=300)
result_label.pack()

result_label_1 = tk.Label(root, text='', wraplength=300)
result_label_1.pack()

root.mainloop()