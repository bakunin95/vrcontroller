import smbus
import math
import time



power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
bus = smbus.SMBus(1)
address = 0x68

bus.write_byte_data(address, power_mgmt_1, 0)


def read(address,adr):
	high = bus.read_byte_data(address, adr)
	low = bus.read_byte_data(address, adr+1)
	val = (high << 8) + low
	return val


def dist(a,b):
	return math.sqrt((a*a)+(b*b))


def get_x_rotation(x,y,z):
	radians = math.atan(x / dist(y,z))
#	return math.degrees(radians)
        return radians

def get_y_rotation(x,y,z):
        radians = 0
        try :
    		radians = math.atan(y / dist(x,z))
	except :
   		pass	
#	return math.degrees(radians)
        return radians


def get_roll(x,y,z):
	return math.atan2(y, z)*180/3.14

def get_pitch(x,y,z):
        return math.atan2(x,dist(y,z))*180/3.14

timestr = time.strftime("%Y%m%d-%H%M%S")

f = open('results/result'+timestr+'.csv', 'w')
gyrosensitivity  = 131;
accelsensitivity = 16384
while True:        	
	GyX = read(address,0x43)/gyrosensitivity
	GyY = read(address,0x45)/gyrosensitivity
	GyZ = read(address,0x47)/gyrosensitivity
#	AcX = read(address,0x3b)/accelsensitivity 
#	AcY = read(address,0x3d)/accelsensitivity
#	AcZ = read(address,0x3f)/accelsensitivity
	AcX = read(address,0x3b)
	AcY = read(address,0x3d)
	AcZ = read(address,0x3f)
	CoX = read(address,0x4A)
	CoY = read(address,0x4C)
	CoZ = read(address,0x4E)
	Xrot = get_x_rotation(AcX,AcY,AcZ)
	Yrot = get_y_rotation(AcX,AcY,AcZ)


	roll  = get_roll(AcX,AcY,AcZ)
	pitch = get_pitch(AcX,AcY,AcZ)

	result = "{} {} {} {} {} {} {} {} {} {} {} {} {}".format(GyX,GyY,GyZ,AcX,AcY,AcZ,CoX,CoY,CoZ,Xrot,Yrot,roll,pitch)
	print(result)
	f.write(result+"\n")

