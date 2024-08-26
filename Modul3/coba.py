# import socket

# # Mendapatkan nama host dari komputer lokal
# host_name = socket.gethostname()

# # Menampilkan nama host
# print("Nama Host:", host_name)

import socket

# Mendapatkan alamat IP dari nama host
host_name = "www.youtube.com"
ip_address = socket.gethostbyname(host_name)

# Menampilkan hasil
print(f"Alamat IP dari {host_name} adalah {ip_address}")
