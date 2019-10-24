import socket
from server import Server

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 8889))
    try:
        sock.sendall(bytes('message', 'ascii'))
    finally:
        sock.close()