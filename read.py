from time import sleep
from datetime import datetime
import time
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()


now = datetime.now()

current_time = now.strftime("%H:%M:%S")

rfid = ''

try:
	print("Hold a tag near the reader")

	while True:
		# GPIO.setwarnings(False)
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
