import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (1024, 786)

i = 0
while True:
	dateiname = "bild_"+str(i)+".jpg"
	camera.capture(dateiname)
	time.sleep(59)
	i += 1
