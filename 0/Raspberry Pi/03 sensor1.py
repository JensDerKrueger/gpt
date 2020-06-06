import sense_hat
sense = sense_hat.SenseHat()

temperatur = sense.get_temperature()
print("Temperatur:",temperatur,"°C")
