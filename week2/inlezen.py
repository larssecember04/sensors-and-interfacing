sensor_file_name = '/sys/bus/w1/devices/28-0417b2507eff/w1_slave'

sensor_file = open(sensor_file_name,'r')
for line in sensor_file:
    print(line)

sensor_file.close()