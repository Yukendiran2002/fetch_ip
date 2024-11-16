import socket
import requests

def get_local_ip():
    """
    Fetches the local IP address of the system.
    """
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except socket.error as e:
        return f"Error fetching local IP: {e}"

def get_public_ip():
    """
    Fetches the public IP address of the system by querying an external service.
    """
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        if response.status_code == 200:
            public_ip = response.json().get('ip')
            return public_ip
        else:
            return "Failed to fetch public IP (non-200 response)."
    except requests.RequestException as e:
        return f"Error fetching public IP: {e}"

if __name__ == "__main__":
    print("Fetching IP addresses...")
    print(f"Local IP: {get_local_ip()}")
    print(f"Public IP: {get_public_ip()}")
