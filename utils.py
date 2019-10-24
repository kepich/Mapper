import socketserver
import threading
import socket

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class Queue:
    def __init__(self, ip, port):
        self.server = ThreadedTCPServer((ip, port), ThreadedTCPRequestHandler)
        self.server.queue = self
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.messages = []
    
    def start_server(self):
        self.server_thread.start()
        print("Server running in thread:", self.server_thread.name)

    def stop_server(self):
        print("*** Server closed! Bye! ***")
        self.server.shutdown()
        self.server.server_close()

    def add(self, message):
        self.messages.append(message)

    def view(self):
        return self.messages

    def get(self):
        return self.messages.pop()

    def exists(self):
        return len(self.messages)

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """
        Request handler class for server
    """
    def handle(self):
        data = self.request.recv(1024)
        print(data)