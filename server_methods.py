import threading
import sockets
import requests
import sys
from config import *

def main_server_loop():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_ADDR, SERVER_PORT)) 
    # Add some address or should it resolve dynamically
    while True:
        server_socket.listen(10)
        sock, addr = server_socket.accept() # Is this correct syntax?
