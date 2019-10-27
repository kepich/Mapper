import socket
import sys
import time
from server import Server

class Mapping_client(Server):
    """
        Class for client
    """
    def handle(self, message):
        """
            Get message from queue
        """
        try:
            recieved = message.decode()
            return recieved
        except Exception as e:
            print("Error: {}".format(e))

        return ''
    
    def inp_env(self):
        """
            Input function
        """
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Enter envoirement (string of 8 chars, ex: TFRLHSPE) or Q to quite: ')
        query = ''
        while True:
            query = input()
            
            if len(query) != 8 or (not query.isalpha()):        # Input correct checking
                if query == 'q' or query == 'Q':
                    break
                else: 
                    print('Incorrect input! Try again!')
            else:
                is_correct = True
                string = query.upper()
                req_symb = ['T', 'F', 'R', 'L', 'H', 'S', 'P', 'E']
                for i in string:
                    if req_symb.count(i) == 0:
                        is_correct = False
                        break
                if is_correct:
                    break
                else:
                    print('Incorrect input! Try again!')
        return query.upper()
    
    def correcting_env(self, old_env):
        """
            Correcting envoirement function
        """
        print(': No matches found! Correcting request...')
        new_env = old_env[1:]
        ch_seq = ['L', 'R', 'H', 'S', 'F']
        for i in ch_seq:
            if new_env.count(i) > 0:
                new_env = new_env.replace(i, 'E')
                break
        
        return new_env
    
    def translate_ans(self, old_ans):
        """
            Translaiting  raw roote to beauty look up
        """
        new_ans = old_ans[1:]
        new_ans = new_ans.replace('L', ', Left ')
        new_ans = new_ans.replace('R', ', Right ')
        new_ans = new_ans.replace('T', ', Top ')
        new_ans = new_ans.replace('B', ', Bottom ')
        new_ans = '[ ' + new_ans[2:-1] + ']'
        return new_ans

    def loop(self, server_ip, server_port):
        """
            Client working loop
        """
        is_resending = False
        while True:
            if not is_resending:
                query = self.inp_env()
                
                if query == 'Q':
                    return

            # Sending message *************************************************
            print('******************************************')
            my_port = 8899
            my_ip = socket.gethostbyname(socket.gethostname())
            
            print(': Sending: {} ...'.format(query))

            query = my_ip + '_' + str(my_port) + '_' + query    # Message change to <...>_<...>_<...>
            amount_of_resending = 5
            temp_tr = 0
            for temp_tr in range(amount_of_resending):
                if self.send(server_ip, server_port, query) == -1:
                    print(': ({} of {})Message is not sended! Resending...'.format(temp_tr + 1, amount_of_resending))
                    time.sleep(1)
                else:
                    break
            else:
                print(': ERROR! Connection refused! Check your internet connection or try again later!')
                continue
            # *****************************************************************

            is_timeout = False
            timeout = 30         # Waiting answer timeout
            print(': Wating answer...')
            for i in range(timeout):                                 # Waiting answer
                time.sleep(1)
                    
                while self.queue.exists():
                    print(': Query result recieved! Checking...')
                    query = self.handle(self.queue.get())
                    i = timeout
                    break
                
                if i == timeout - 1:        # Timeout error
                    print(': Wating time runs out! Server not available! Try again later!')
                elif i == timeout:
                    break
            
            if not is_timeout:
                if query[0] == 'N':                         # Correcting or translating answer
                    query = self.correcting_env(query)
                    is_resending = True
                else:
                    print(self.translate_ans(query))
                    is_resending = False
            else:
                timeout = False

if __name__ == "__main__":
    print("Client started...")
    
    my_port = 8899
    my_ip = socket.gethostbyname(socket.gethostname())
    
    server_ip = socket.gethostbyname(socket.gethostname())
    server_port = 8889
    
    app = Mapping_client(my_ip, my_port)
    app.start_server()
    app.loop(server_ip, server_port)
    print("*** Client closed! Bye! ***")
    app.stop_server()