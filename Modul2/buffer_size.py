import socket

def get_default_buffer_size():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sndbuf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Default Send Buffer Size: %d bytes" % sndbuf) 

    rcvbuf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Default Receive Buffer Size: %d bytes" % rcvbuf)

if _name_ == "_main_":
    get_default_buffer_size()