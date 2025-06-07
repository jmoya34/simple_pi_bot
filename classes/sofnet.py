import socket
import threading
import queue
import json
import time

class MessageServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self.__start)
        self.thread.daemon = True
        self.thread.start()

    def __start(self): 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data: break
                    try:
                        # Decode bytes to string and parse JSON
                        message = json.loads(data.decode('utf-8'))
                        print("Received JSON:", message)
                    except json.JSONDecodeError:
                        print("Received invalid JSON")

class MessageClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.msgQueue = queue.Queue()
        self.threadRunning = False
        self.msgThread = threading.Thread(target=self.__atemptConnection, args=())
        self.msgThread.daemon = True
        self.msgThread.start()

    def __atemptConnection(self):
        while True:
            try: 
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self.host, self.port))
                    #convert the msg string into bytes
                    self.threadRunning = True
                    while True:
                        msg = self.msgQueue.get()
                        if msg is not None:
                            json_data = json.dumps(msg)
                            encoded_data = json_data.encode('utf-8') 
                            s.sendall(encoded_data)
                print('Confirmation from server', repr(data))
            except:
                self.threadRunning = False
                print("connection issue. IP could be incorrect")
                time.sleep(10)
        

    def send(self, msg: dict):
        self.msgQueue.put(msg)
        if not self.threadRunning:
            print("Unable to send message currently...")