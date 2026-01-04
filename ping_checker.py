import subprocess
import sys
import platform

def ping_host(host):
    """
    Pings a host to check if it's online.
    """
    try:
        # Determine the correct ping parameter based on the OS
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        
        # Use the system's ping command
        command = ['ping', param, '1', host]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            print(f"{host} is online.")
        else:
            print(f"{host} is offline.")
    except FileNotFoundError:
        print("Error: 'ping' command not found. Please ensure it's installed and in your system's PATH.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ping_check.py <hostname_or_ip>")
        sys.exit(1)
        
    hostname = sys.argv[1]
    ping_host(hostname)
