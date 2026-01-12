import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

open_ports = []

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))
        if result == 0:
            service = COMMON_SERVICES.get(port, "Unknown")
            print(f"[OPEN] Port {port} ({service})")
            open_ports.append(f"Port {port} ({service})")

        sock.close()
    except:
        pass


def main():
    target = input("Enter target IP or hostname: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\nScanning {target}...\n")

    futures = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            futures.append(executor.submit(scan_port, target, port))

        # ✅ Wait for all threads to complete
        for future in as_completed(futures):
            pass

    # ✅ NOW the prompt will always appear
    if open_ports:
        choice = input("\nSave results to file? (y/n): ").lower()
        if choice == 'y':
            with open("scan_results.txt", "w") as f:
                for port in open_ports:
                    f.write(port + "\n")
            print("Results saved to scan_results.txt")
    else:
        print("No open ports found.")

    print("\nScan completed.")


if __name__ == "__main__":
    main()
