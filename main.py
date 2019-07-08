import pycom
import time

pycom.heartbeat(False)

pycom.rgbled(0x111111)

color = [0x0000FF, 0x00F0F0, 0x00F000, 0x00F0F0, 0x0FF00F, 0xF00000, 0x0FFF00, 0xF00FF0]

i2c_dev = I2CAdapter()

if (i2c_dev.scan()):

    sensor = bme680.BME680(i2c_device=i2c_dev)

    # These oversampling settings can be tweaked to
    # change the balance between accuracy and noise in
    # the data.
    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)
    index = 0
    while True:
            if sensor.get_sensor_data():
                output = "{} C, {} hPa, {} RH, {} RES,".format(
                    sensor.data.temperature,
                    sensor.data.pressure,
                    sensor.data.humidity,
                    sensor.data.gas_resistance)

                s.send(str(sensor.data.temperature)+str(sensor.data.humidity))
                #s.send('hello')

                #print(str(sensor.data.temperature))
                print(output)
                pycom.rgbled(color[index])
                index += 1
                if(index > 7):
                    index = 0
                time.sleep(60)
