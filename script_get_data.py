# libraries
import seeed_dht
import seeed_si114x
from grove.grove_moisture_sensor import GroveMoistureSensor
from grove.factory import Factory
import csv
import time
import datetime

# Initial variables
dht_sensor = seeed_dht.DHT("11", 16)
sunlight_sensor = seeed_si114x.grove_si114x()
moisture_sensor = GroveMoistureSensor(0)
button_write = Factory.getButton("GPIO-LOW", 22)
button_reset = Factory.getButton("GPIO-LOW", 23)

# File header
header = ['avgtemp_c','avghumidity','uv','visible','ir','soil_moisture', 'soil_moisture_status','date']

def main():
    while True:
        # If the WHITE button was pressed then
        # the led will CONTINUE OFF and and all data will be DELETED from the file
        if button_reset.is_pressed():
            with open('data.csv', 'w', newline='') as file:
                file.truncate()
        
        # If the GREEN button was pressed then
        # the led will LIGHT UP and the data is being SAVED correctly
        elif button_write.is_pressed():
            with open('data.csv', 'r+', newline='') as file:
                reader = csv.reader(file)
                writer = csv.writer(file)
                
                # If the file was EMPTY then the header is written 
                if [] == [row for row in reader]:
                    writer.writerow(header)
                
                # Switch at convenience. max_count: max number of iterations
                initial_count = 0
                max_count = 50
                
                while initial_count < max_count:

                    # DHT sensor
                    humidity, temperature = dht_sensor.read()
                    
                    # Sunlight sensor
                    visible = sunlight_sensor.ReadVisible
                    UV = sunlight_sensor.ReadUV/100 
                    IR = sunlight_sensor.ReadIR
                    
                    # Moisture sensor
                    soil_moisture = moisture_sensor.moisture
                    if 0 <= soil_moisture and soil_moisture < 300:
                        soil_moisture_status = 'dry'
                    elif 300 <= soil_moisture and soil_moisture < 600:
                        soil_moisture_status = 'moist'
                    else:
                        soil_moisture_status = 'wet'
                    
                    # Get current date
                    time_now = datetime.datetime.now().strftime("%d/%m/%Y")
                    
                    # Write data in CSV file
                    writer.writerow([temperature, humidity, UV, visible, IR, soil_moisture, soil_moisture_status, time_now])
                    print([temperature, humidity, UV, visible, IR, soil_moisture, soil_moisture_status, time_now])                    
                    # Timeout between each iteration
                    time.sleep(0.25)
                    
                    initial_count+=1

if __name__  == '__main__':
    main()
    
    
# Referencias
# DHT sensor
# https://wiki.seeedstudio.com/Grove-TemperatureAndHumidity_Sensor/
# Sunlight sensor
# https://wiki.seeedstudio.com/Grove-Sunlight_Sensor/
# Capacitive Moisture Sensor (Corrosion Resistant)
# https://wiki.seeedstudio.com/Grove-Capacitive_Moisture_Sensor-Corrosion-Resistant/
# Dual Button
# https://wiki.seeedstudio.com/Grove-Dual-Button/