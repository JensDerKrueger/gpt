import time
import sense_hat

def msleep(x):
	time.sleep(x / 1000.0)

sense = sense_hat.SenseHat()
minT = sense.get_temperature()
maxT = minT+0.01

def tuppleLerp(t1, t2, alpha):
	return tuple([int(item1*alpha + item2*(1-alpha)) for item1, item2 in zip(t1, t2)])

def temp2color(temp):
	remap = (temp-minT)/(maxT-minT)
	remap = min(1,max(0,remap))

	red = (255,0,0)
	blue = (0,0,255)
	return tuppleLerp(red, blue, remap)

while True:
	t = sense.get_temperature()
	if t < minT:
		print("New Min. Temp",t,"°C")
		minT = t
	if t > maxT:
		print("New Max. Temp",t,"°C")
		maxT = t
	sense.clear(temp2color(t))
	msleep(10)