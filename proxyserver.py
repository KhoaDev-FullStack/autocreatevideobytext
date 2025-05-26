import socket
import threading
import signal
import sys
from config import config

class ProxyServer:
    def __init__(self):
        # shutdow on ctrl + c
        signal.signal(signal.SIGINT , self.shutdown)

        #create  a tcp socket
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #re-use socket
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

        #bind
        self.serverSocket.bind((config["HOST_NAME"], config["BIND_PORT"]))

        self.serverSocket.listen(10)

        self.__client = {}
    def start(self):
        while True:
            clientSocket, client_address = self.serverSocket.accept()
            client_name = f"{client_address[0]}: {client_address[1]}"
            print(f"[+] Connection from {client_name}")

            thread = threading.Thread(
                name = client_name,
                target=self.proxy_thread,
                args = (clientSocket, client_address)
            )

            thread.setDaemon(True)
            thread.start()

    def proxy_thread(self, connect, client_address):
        config= {
            'MAX_REQUEST_LEN':4096,
             'CONNECT_TIMEOUT':5
        }

         # :: -  format -  ::
         # GET http://example.com/ HTTP/1.1
         # Host: example.com
         # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
         # Accept: text/html,application/xhtml+xml,application/xml;q=0.9
         # Accept-Language: en-US,en;q=0.5
         # Connection: keep-alive


        try:
            # recive data
            request = connect.recv(config["MAX_REQUEST_LEN"])
            #take first line
            first_line = request.decode().slip('\n')[0]
            #take url
            url = first_line.slip(" ")[1]   # http://example.com/

            http_pos = url.finf("://")

            if (http_pos == -1):
                temp = url
            else:
                temp = url[(http_pos+3):]

            port_pos = temp.find(":")
            



    