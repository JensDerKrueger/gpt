#!/usr/bin/env python3

import picamera
from time import sleep
from datetime import datetime, time
import subprocess
import sys
import os

print("Initializing Rasperry Pi Camera")
camera = picamera.PiCamera()
camera.resolution = (1296, 972)
camera.annotate_text_size = 20
camera.rotation = 90
camera.start_preview()
sleep(5)

# change this to your server URL
server = "username@serverurl/path/filename.mp4"

convertToBW = False

while True:
	missedToday = datetime.today().time().hour*60+datetime.today().time().minute
	output = "video%s.mp4" % datetime.today().date().day

	print("Capturing images for video",output)
	i = 0
	while not (datetime.today().time().hour == 23 and datetime.today().time().minute == 59):
		waitTime = 61 - datetime.today().time().second
		print("  ", datetime.today().time(), "waiting", waitTime, "seconds for the next minute to begin")
		sleep(waitTime)
		filename = "image_%s.jpg" % i
		i += 1
		print("  ", datetime.today().time(),"capturing",filename)
		camera.annotate_text = datetime.now().strftime("%d.%m.%Y %H:%M")
		camera.capture(filename)

	try:
		print("Rendering video",output)
		
		if (convertToBW):
			params = ["avconv", "-n", "-r", "30", "-i", "image_%d.jpg", "-r", "30", "-vcodec", "libx264", "-crf", "20", "-g", "15", "-filter:v", "lutyuv=u=128:v=128", "-pix_fmt", "yuvj420p", output]
		else:
			params = ["avconv", "-n", "-r", "30", "-i", "image_%d.jpg", "-r", "30", "-vcodec", "libx264", "-crf", "20", "-g", "15", "-pix_fmt", "yuvj420p", output]
			
		subprocess.check_call(params)
		print(datetime.today().time(), "done with video", output)
	except:
		print(datetime.today().time(), "error during video encoding of file", output, file=sys.stderr)
		continue

	try:
		print(datetime.today().time(), "Uploading video",output)
		params = ["scp", output, server]
		subprocess.check_call(params)
		print(datetime.today().time(), "done with upload of", output)
	except:
		print(datetime.today().time(), "error during upload of", output, file=sys.stderr)
		continue

	try:
		os.remove(output)
	except:
		print(datetime.today().time(), "unable to delete the file", output, file=sys.stderr)

# never reached but here for completeness
camera.stop_preview()
