#!/usr/bin/env python3

import sys
from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM

class elfin:
    def __init__(self):
        self.end_msg = ",;"

    def connect(self, SERVER_IP, PORT_NUMBER, SIZE, rbtID):
        mySocket = socket(AF_INET, SOCK_STREAM)
        mySocket.connect((SERVER_IP, PORT_NUMBER))

        self.size = SIZE
        self.rbtID = str(rbtID)
        self.mySocket = mySocket

    def send(self, message):
        self.mySocket.sendall(message.encode('utf-8'))
        data = self.mySocket.recv(self.size).decode('utf-8').split(',')
        status = self.check_status(data)
        if status:
            if len(data) > 3:
                return data[2:-1]
        return status

    def check_status(self, recv_message):
        status = recv_message[1]
        if status == 'OK':
            return True

        elif status == 'Fail':
            print("Error code: ", recv_message[2])
            return False

    def Electrify(self):
        """
        Function: Power the robot
        :return:
            if Error Return False
            if not Error Return True
        """
        message = "Electrify" + self.end_msg
        status = self.send(message)
        return status

    def SetOverride(self, override):
        """
        function: Set speed ratio
        :return:
            if Error Return False
            if not Error Return True
        """

        message = "SetOverride" + self.rbtID + ',' + str(override) + self.end_msg
        status = self.send(message)
        return status

    def ReadPcsActualPos(self):
        """Function: Get the actual position of the space coordinate
        :return:
            if True Return x,y,z,a,b,c
            if Error Return False
        """
        message = "ReadPcsActualPos," + self.rbtID + self.end_msg
        coord = self.send(message)
        if coord:
            return [float(s) for s in coord]

        return coord

    def MoveL(self, target):
        """
        function: Robot moves straight to the specified space coordinates
        :param target:[X,Y,Z,RX,RY,RZ]
        :return:
        """
        target = [str(s) for s in target]
        target = (",".join(target))
        message = "MoveL," + self.rbtID + ',' + target + self.end_msg
        print(message)
        return self.send(message)