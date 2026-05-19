'''
This module needs to answer one question: what is the router's IP address?
To answer it, it needs to do three things:

    1. Check which network interfaces your computer has (WiFi, Ethernet, etc.)
    2. Filter the ones that are active and connected
   3.  Calculate the router's IP from your own IP


'''
import subprocess

def get_gateway_ip():
    gateway = None
    result = subprocess.run(['route', 'print', '0.0.0.0'], capture_output=True, text=True);  # Check the default route
    lines = result.stdout.splitlines()

    for par in lines:
        clear = par.strip()
        if clear.startswith("0.0.0.0"):
            parts = clear.split()
            gateway = parts[2] # Select Gateway
            return gateway
    return None
