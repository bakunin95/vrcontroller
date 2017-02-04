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
	return math.degrees(radians)

def get_y_rotation(x,y,z):
	radians = math.atan(y / dist(x,z))
	return math.degrees(radians)


timestr = time.strftime("%Y%m%d-%H%M%S")

f = open('result'+timestr+'.csv', 'w')
gyrosensitivity  = 131;
accelsensitivity = 16384
while True:        	
	GyX = read(address,0x43)/gyrosensitivity
	GyY = read(address,0x45)/gyrosensitivity
	GyZ = read(address,0x47)/gyrosensitivity
	AcX = read(address,0x3b)/accelsensitivity 
	AcY = read(address,0x3d)/accelsensitivity
	AcZ = read(address,0x3f)/accelsensitivity
	CoX = read(address,0x4a)
	CoY = read(address,0x4c)
	CoZ = read(address,0x4e)
	Xrot = get_x_rotation(AcX,AcY,AcZ)
	Yrot = get_y_rotation(AcX,AcY,AcZ)

	result = "{} {} {} {} {} {} {} {} {} {} {}".format(GyX,GyY,GyZ,AcX,AcY,AcZ,CoX,CoY,CoZ,Xrot,Yrot)
	print(result)
	f.write(result+"\n")

