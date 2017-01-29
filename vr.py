import smbus

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




while True:
	print("Coord: {} {} {} - {} {} {}".format(read(address,0x43),read(address,0x45),read(address,0x47),read(address,0x3b),read(address,0x3d),read(address,0x3f)))
	print(read(address,0x00))

