# import threading
# import socket
import queue
from classes.sofnet import MessageServer, MessageClient
import time

server = MessageServer('', 8008)
client = MessageClient('192.168.254.20', 8008)

while True:
    test_dict = {'LAnalog': 1.008, 'RAnalog': 0.003}
    client.send(test_dict)
    time.sleep(1)


    my_dict = {
        'RAnalog': 0,
        'LAnalog': 0,
    }

    while True:
        events; 
        for event in events:
            # event.code is the type of input
            # event.state is the input value

            # Condition statement
            if event.code == 'Ranalog':
                my_dict['RAnalog'] = event.state 
            # do the rest
        
        return my_dict

