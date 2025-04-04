import socket
import argparse

def scan_port(ip, port):
    """Check if a specific port is open."""
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to avoid long delays

        # Try connecting to the port
        result = sock.connect_ex((ip, port))  # Returns 0 if open, else error code
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

def scan_ports(ip, start_port, end_port):
    """Scan a range of ports on the given IP address."""
    print(f"\n🔍 Scanning {ip} from port {start_port} to {end_port}...\n")
    
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("ip", help="Target IP address")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    args = parser.parse_args()

    scan_ports(args.ip, args.start, args.end)
