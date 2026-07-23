import socket
import hashlib
import secrets
import string

def port_scanner():
    ip = input("Enter IP: ")

    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3389]

    print("\nOpen Ports")

    for port in ports:
        s = socket.socket()
        s.settimeout(0.3)

        if s.connect_ex((ip, port)) == 0:
            print(f"Port {port}: OPEN")

        s.close()


def hash_file():
    filename = input("File name: ")

    try:
        with open(filename, "rb") as f:
            print(hashlib.sha256(f.read()).hexdigest())
    except FileNotFoundError:
        print("File not found.")


def password_generator():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"

    password = "".join(secrets.choice(chars) for _ in range(20))

    print(password)


def dns_lookup():
    domain = input("Domain: ")

    try:
        print(socket.gethostbyname(domain))
    except socket.gaierror:
        print("Domain not found.")


def banner_grab():
    ip = input("IP: ")
    port = int(input("Port: "))

    try:
        s = socket.socket()
        s.settimeout(2)

        s.connect((ip, port))

        print(s.recv(1024).decode(errors="ignore"))

        s.close()

    except:
        print("Unable to grab banner.")


while True:

    print("""
CyberToolkit
---------------------
1. Port Scanner
2. SHA256 File Hash
3. Password Generator
4. DNS Lookup
5. Banner Grabber
6. Quit
""")

    choice = input("Choice: ")

    if choice == "1":
        port_scanner()

    elif choice == "2":
        hash_file()

    elif choice == "3":
        password_generator()

    elif choice == "4":
        dns_lookup()

    elif choice == "5":
        banner_grab()

    elif choice == "6":
        break

    else:
        print("Invalid choice.")
