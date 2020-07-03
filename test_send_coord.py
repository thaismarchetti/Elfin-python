import elfin
import time

SERVER_IP   = '169.254.153.251'
PORT_NUMBER = 10003
SIZE = 1024
rbtID = 0

cobot = elfin.elfin()
cobot.connect(SERVER_IP, PORT_NUMBER, SIZE, rbtID)
print(cobot.ReadPcsActualPos())

target = [500.0, 0.0, 600.0, -90.0, 51.0, -106.0]
print("starting move")
print(cobot.MoveL(target))
status = cobot.ReadMoveState()
while status == 1009:
    time.sleep(2)
    print("moving...")
    print(cobot.ReadPcsActualPos())
    status = cobot.ReadMoveState()
    print(status)
print("end move")
print(cobot.ReadPcsActualPos())