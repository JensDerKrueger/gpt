import picamera

camera = picamera.PiCamera()
camera.start_recording("video.h264")
sleep(10)
camera.stop_recording()