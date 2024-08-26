import socket

server_sockeet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
server_socket.bind(server_address)

# mendengarkan koneksi masuk
server_socket.listen(5)
print("Server listening on {}:{}".format(*server_address))

while True:
    # Menerima koneksi dari client
    client_socket, client_addres = server_socket.accept()
    print("Received connection from {}:{}.format(*client_address)")
    
    #menerima dan mengirim data
    data = client_socket.recv(1024)
    print("received data: {}".format(data.decode('utf-8')))
    client_sockt.sendall(b"Hello, client!")
    
    # menutup koneksi
    client_socket.close()