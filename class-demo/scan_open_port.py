# Import module
import socket
import argparse

# Create a socket object
def scan_port(ip, port):
    """Check if a scpecific port is open on a given IP address."""
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout for the connection attempt
        s.settimeout(1)

        # Try connecting to the IP address and port
        result = s.connect_ex((ip, port))

        # If condition statement
        if result == 0:
            print(f"[+] Port {port} is open on {ip}")
        else:
            print(f"[-] Port {port} is closed on {ip}")
        s.close()
    except Exception as e:
        print(f"[-] Error scannin port {port} on {ip}: {e}")


def scan_ports(ip, start_port, end_port):
    """Scan a range of ports on the given IP address."""
    print(f"\n Scanning {ip} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

# The main program
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This tool was created by webdeves cybersecurity students.')
    parser.add_argument("ip", help="Target IP address")
    parser.add_argument("--start", type=int, default=1, help="Specify starting port (defaut: 1)")
    parser.add_argument("--end", type=int, default=1024, help="Specify the ending port (default: 1024)")

    args = parser.parse_args()


    scan_ports(args.ip, args.start, args.end)