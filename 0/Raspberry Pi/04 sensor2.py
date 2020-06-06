import sense_hat
sense = sense_hat.SenseHat()

temperatur1 = sense.get_temperature()
temperatur2 = sense.get_temperature_from_pressure()
feuchtigkeit = sense.get_humidity()
luftdruck = sense.get_pressure()

print("Temperatur Sensor 1:",temperatur1,"°C")
print("Temperatur Sensor 2:",temperatur2,"°C")
print("Luftfeuchtigkeit:",feuchtigkeit,"%")
print("Luftdruck:",luftdruck,"hPa")