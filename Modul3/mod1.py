import socket

def nslookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"Nama domain: {domain}")
        print(f"Alamat IP: {ip_address}")
    except socket.gaierror:
        print(f"Tidak dapat menemukan alamat IP untuk domain: {domain}")
        
if __name__ == "__main__":
    domain = input("Masukkan domain yang ingin anda cek:")
    nslookup(domain)