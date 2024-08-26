import sys
import socket

def main():

    host = input("Masukkan alamat host: ")
    port = int(input("Masukkan port: "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
        print("Connected to %s on port %d " %(host,port))
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(1)


if __name__ == '__main__':
    main()