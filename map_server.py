from server import Server
from db import DB
import http.client
from sys import argv

class Mapping_server(Server):
    """
        Run with argv = \t to create new database
    """
    def __init__(self, ip, port, is_new_db = False):
        super(Mapping_server, self).__init__(ip, port)
        self.data_base = DB(is_new_db)
    def handle(self, message):
        try:
            print("Got: {}".format(message))
            sender_info = (message.decode()).split('_')
            result = self.data_base.Get_By_Env(sender_info[2])
            print("Send: {}".format(result))
            self.send(sender_info[0], int(sender_info[1]), result)
        except Exception as e:
            print("Error: {}".format(e))


if __name__ == "__main__":
    print("Server started...")
    my_ip = "localhost"
    if len(argv) == 2 and argv[1] == '\\t':
        app = Mapping_server(my_ip, 8889, True)
    else:
        app = Mapping_server(my_ip, 8889)

    app.start_server()
    app.loop()
    app.stop_server()