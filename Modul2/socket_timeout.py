# Ghaida Fasya Yuthika Afifah
# D4TI - 2B
# 714220031


# Mengatur dan mendapatkan default socket timeout

import socket

def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Default socket timeout: %" %.gettimeout())
    s.settimeout(100)
    print("Current socket timeout: %" %.gettimeout())
if __name__ == '__main__':
    test_socket_timeout()