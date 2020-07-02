import elfin

SERVER_IP   = '127.0.0.1'
PORT_NUMBER = 5000
SIZE = 1024
rbtID = 0

cobot = elfin.elfin()
cobot.connect(SERVER_IP, PORT_NUMBER, SIZE, rbtID)
target = [1.5,2.4,3.4,4.7,5.8,6.8]
a = cobot.MoveL(target)
print(a)