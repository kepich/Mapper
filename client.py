import socket
import sys
import time
from server import Server

class Mapping_client(Server):
    def handle(self, message):
        try:
            recieved = message.decode()
            return recieved
        except Exception as e:
            print("Error: {}".format(e))

        return ''
    
    def inp_env(self):
        print('Enter envoirement (string of 8 chars, ex: TFRLHSPE): ')
        query = ''
        while True:
            query = input()
            
            if len(query) != 8 or (not query.isalpha()):
                if query == 'q' or query == 'Q':
                    break
                else: 
                    print('Incorrect input! Try again!')
            else:
                break
        return query.upper()
    
    def correcting_env(self, old_env):
        print(': No matches found! Correcting request...')
        new_env = old_env[1:]
        ch_seq = ['L', 'R', 'H', 'S', 'F']
        for i in ch_seq:
            if new_env.count(i) > 0:
                new_env = new_env.replace(i, 'E')
                break
        
        return new_env
    
    def translate_ans(self, old_ans):
        new_ans = old_ans[1:]
        new_ans = new_ans.replace('L', ', Left ')
        new_ans = new_ans.replace('R', ', Right ')
        new_ans = new_ans.replace('T', ', Top ')
        new_ans = new_ans.replace('B', ', Bottom ')
        new_ans = '[ ' + new_ans[2:-1] + ']'
        return new_ans

    def loop(self, server_ip, server_port):
        is_resending = False
        while True:
            if not is_resending:
                query = self.inp_env()
                
                if query == 'Q':
                    return

            # Sending message *************************************************
            print('******************************************')
            my_port = 8899
            my_ip = "localhost"
            
            print(': Sending: {} ...'.format(query))

            query = my_ip + '_' + str(my_port) + '_' + query
            self.send(server_ip, server_port, query)
            # *****************************************************************

            recieved = False
            print(': Wating answer...')
            while not recieved:
                time.sleep(1)
                while self.queue.exists():
                    print(': Query result recieved! Checking...')
                    query = self.handle(self.queue.get())
                    recieved = True
                    break
            
            if query[0] == 'N':
                query = self.correcting_env(query)
                is_resending = True
            else:
                print(self.translate_ans(query))
                is_resending = False

if __name__ == "__main__":
    print("Client started...")
    
    my_port = 8899
    my_ip = "localhost"
    
    server_ip = "127.0.0.1"
    server_port = 8889
    
    app = Mapping_client(my_ip, my_port)
    app.start_server()
    app.loop(server_ip, server_port)
    app.stop_server()