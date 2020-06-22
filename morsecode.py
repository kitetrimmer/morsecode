import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT,initial=GPIO.LOW)

# define the morse code dictionary - 1 = dit, 2 = dah, 0 = word break
mc =  {'A':(1,2),
	'B':(2,1,1,1),
	'C':(2,1,2,1),
	'D':(2,1,1),
	'E':(1,),  # AHA!  Need a comma after a single value tuple for len(tuple)
	'F':(1,1,2,1),
	'G':(2,2,1),
	'H':(1,1,1,1),
	'I':(1,1),
	'J':(1,2,2,2),
	'K':(2,1,2),
	'L':(1,2,1,1),
	'M':(2,2),
	'N':(2,1),
	'O':(2,2,2),
	'P':(1,2,2,1),
	'Q':(2,2,1,2),
	'R':(1,2,1),
	'S':(1,1,1),
	'T':(2,),
	'U':(1,1,2),
	'V':(1,1,1,2),
	'W':(1,2,2),
	'X':(2,1,1,2),
	'Y':(2,1,2,2),
	'Z':(2,2,1,1),
	' ':(0,),
	'1':(1,2,2,2,2),
	'2':(1,1,2,2,2),
	'3':(1,1,1,2,2),
	'4':(1,1,1,1,2),
	'5':(1,1,1,1,1),
	'6':(2,1,1,1,1),
	'7':(2,2,1,1,1),
	'8':(2,2,2,1,1),
	'9':(2,2,2,2,1),
	'0':(2,2,2,2,2)}

unit = .25


mess=input('message: ')
mess = mess.upper()

for cn in range (0,len(mess)):
	for x in range (0,len(mc[mess[cn]])):
		if(mc[mess[cn]][x] == 1):
		#	print ('dit')
			GPIO.output(8,GPIO.HIGH)
			sleep(unit)
			GPIO.output(8,GPIO.LOW)
			sleep(unit)
		elif(mc[mess[cn]][x] == 2):
		#	print ('dah')
			GPIO.output(8,GPIO.HIGH)
			sleep(unit*3)
			GPIO.output(8,GPIO.LOW)
			sleep(unit)
		elif(mc[mess[cn]][x] == 0):
		#	print ('New Word')
			GPIO.output(8,GPIO.LOW)
			sleep(unit*6)
		else:
			print('Hmmm....')
	#print('New Letter')
	GPIO.output(8,GPIO.LOW)
	sleep(unit*3)



