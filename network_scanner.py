import socket

print("=== Basic Network Scanner ===")

target = input("Enter target IP : ")

ports = [21, 22, 23, 25, 53, 80, 110, 443, 8000]

print(f"\nScanning {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    sock.close()
    
    if not open_ports:
    print("No open ports found.")

print("\nScan completed.")
