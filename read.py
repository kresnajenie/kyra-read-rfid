from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

GPIO.setwarnings(false)

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

rfid = ''

try:
	while True:
		print("Hold a tag near the reader")
		id, text= reader.read()
		if id != rfid:
			print("ID: %s\nTIME: %s" % (id, current_time))
			time.sleep(2)
		else:
			pass
		
		rfid = id
except KeyboardInterrupt:
	GPIO.cleanup()
	raise
