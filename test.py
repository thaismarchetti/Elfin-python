import elfin

SERVER_IP   = '169.254.153.251'
PORT_NUMBER = 10003

SIZE = 1024
rbtID = 0

# for testing without the robot uncomment the following lines
#SERVER_IP   = '127.0.0.1'
#PORT_NUMBER = 5000

cobot = elfin.elfin()
cobot.connect(SERVER_IP, PORT_NUMBER, SIZE, rbtID)
#cobot.Electrify()
#cobot.StartMaster()
cobot.GrpPowerOn()
print("done start")
cobot.SetOverride(0.05)
#cobot.MoveHoming()

print(cobot.ReadPcsActualPos())


#target = [1.5,2.4,3.4,4.7,5.8,6.8]
#a = cobot.MoveL(target)
#print(a)