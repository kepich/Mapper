from server import Server
from level_map import Level_map
from db import DB

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
    app = Mapping_server("localhost", 8889)
    app.start_server()
    app.loop()
    app.stop_server()