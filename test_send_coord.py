import elfin
import time

SERVER_IP   = '127.0.0.1'
PORT_NUMBER = 10003
SIZE = 1024
rbtID = 0

cobot = elfin.elfin()
cobot.connect(SERVER_IP, PORT_NUMBER, SIZE, rbtID)
print(cobot.ReadPcsActualPos())


target = [0,0,0,0,0,0]
print("starting move")
print(cobot.MoveJ(target))
status = cobot.ReadMoveState()
while status == 1009:
    time.sleep(2)
    print("moving...")
    print(cobot.ReadPcsActualPos())
    status = cobot.ReadMoveState()
    print(status)
print("end move")
print(cobot.ReadPcsActualPos())

target = [0,0,90,0,90,0]
print("starting move")
print(cobot.MoveJ(target))
status = cobot.ReadMoveState()
while status == 1009:
    time.sleep(2)
    print("moving...")
    print(cobot.ReadPcsActualPos())
    status = cobot.ReadMoveState()
    print(status)
print("end move")
print(cobot.ReadPcsActualPos())

target = [0,1,10]
print("starting move")
print(cobot.MoveRelL(target))
status = cobot.ReadMoveState()
while status == 1009:
    time.sleep(2)
    print("moving...")
    print(cobot.ReadPcsActualPos())
    status = cobot.ReadMoveState()
    print(status)
print("end move")
print(cobot.ReadPcsActualPos())

target = [2,1,10]
print("starting move")
print(cobot.MoveRelJ(target))
status = cobot.ReadMoveState()
while status == 1009:
    time.sleep(2)
    print("moving...")
    print(cobot.ReadPcsActualPos())
    status = cobot.ReadMoveState()
    print(status)
print("end move")
print(cobot.ReadPcsActualPos())









