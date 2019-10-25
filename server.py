import socket
import time
from utils import Queue

class Server:
    """
    Server class
    """

    def __init__(self, ip, port):
        self.queue = Queue(ip, port)
    
    def start_server(self):
        """
        Server starting function
        """
        self.queue.start_server()

    def stop_server(self):
        """
        Server stopping function
        """
        self.queue.stop_server()

    def loop(self):
        """
        Checking recieving messages function
        """
        while True:
            time.sleep(1)
            while self.queue.exists():
                self.handle(self.queue.get())
    
    def handle(self, message):
        """
        Prototype
        """
        pass

    def send(self, ip, port, message):
        """
        Sending function
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        try:
            sock.sendall(bytes(message, 'ascii'))
        finally:
            sock.close()