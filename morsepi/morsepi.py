#program for using an led to communicate in morse code

from gpiozero import LED
from time import sleep
import string as string
led = LED(18) #set the default led to gpio pin 18

MORSE_DICT = {'A':'.-', 'B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.',
'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..','M':'--','N':'-.','O':'---',
'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--',
'X':'-..-','Y':'-.--','Z':'--..','1':'.----','2':'..---','3':'...--','4':'....-',
'5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',',':'--..--',
'.':'.-.-.-','?':'..--..','/':'-..-.','-':'-....-','(':'-.--.',')':'-.--..-'}

def setLED(pin):
	led = LED(pin)

def _dot():
	led.on()
	sleep(0.5)
	led.off()
	sleep(0.15)

def _dash():
	led.on()
	sleep(1.5)
	led.off()
	sleep(0.15)

def _space():
	led.off()
	sleep(1.5)

def _pause():
	led.off()
	sleep(0.5)

def morseEncrypt(string):
	string = string.upper()
	cipher = ' '
	for letter in string:
		if letter != ' ':
			cipher += MORSE_DICT[letter] + ' '
		else:
			cipher += ' '
	return cipher

def morseSpeak(string):
	encoded_string = morseEncrypt(string)
	for character in encoded_string:
		if character == '-':
			_dash()
		elif character == '.':
			_dot()
		elif character == ' ':
			_pause()
		else:
			_space()


sleep(0.5)
morseSpeak('hi')
