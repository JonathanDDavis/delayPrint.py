import time
import random
import sys

def delayPrint(x):
	for i in x:
			sys.stdout.write(i)
			sys.stdout.flush()
			time.sleep(0.25)
delayPrint("Hello,World!")
