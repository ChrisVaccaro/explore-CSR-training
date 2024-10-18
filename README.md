# ExploreCSR 2023 
The demo is about getting data from sensors to learn clustering techniques.

### References
- DHT sensor: https://wiki.seeedstudio.com/Grove-TemperatureAndHumidity_Sensor/
  - (without virtualenv) `sudo pip install git+https://github.com/Seeed-Studio/Seeed_Python_DHT.git --break-system-packages`
- Sunlight sensor: https://wiki.seeedstudio.com/Grove-Sunlight_Sensor/
  - (without virtualenv) `sudo pip install git+https://github.com/Seeed-Studio/Seeed_Python_SI114X.git --break-system-packages`
- Capacitive Moisture Sensor (Corrosion Resistant): https://wiki.seeedstudio.com/Grove-Capacitive_Moisture_Sensor-Corrosion-Resistant/
- Dual Button: https://wiki.seeedstudio.com/Grove-Dual-Button/
  - (without virtualenv) `sudo pip install git+https://github.com/Seeed-Studio/grove.py --break-system-packages`
 
### Errors
- Button function isAlive
  -  `pip install rpi-lgpio --break-system-packages`
- No I2C
  - `i2cdetect -y 1`
  - `sudo find / -name adc.py`
  - `sudo nano /usr/local/lib/python3.11/dist-packages/grove/adc.py`
  - Replace all '0x08' by the new address (i2cdetect)
