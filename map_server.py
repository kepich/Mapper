from server import Server
from level_map import Level_map
from db import DB
import http.client

class Mapping_server(Server):
    def __init__(self, ip, port):
        super(Mapping_server, self).__init__(ip, port)
        self.data_base = DB()
    def handle(self, message):
        try:
            print("Got: {}".format(message))
            sender_info = (message.decode()).split('_')
            self.send(sender_info[0], int(sender_info[1]), self.data_base.Get_By_Env(sender_info[2]))
        except Exception as e:
            print("Error: {}".format(e))


if __name__ == "__main__":
    print("Server started...")
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    my_ip = conn.getresponse().read().decode()
    my_ip = "localhost"
    app = Mapping_server(my_ip, 8889)
    app.start_server()
    app.loop()
    app.stop_server()