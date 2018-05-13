import random
from subprocess import call

words = 'prjcm?546kyb ox3gu8$t#ihz1%l&fve7!da2s9@q^n0w'	#encryption key

def banner():
	print """

                                                         
 _____ _____     _____                     _   _         
|     |  |  |___|   __|___ ___ ___ _ _ ___| |_|_|___ ___ 
| | | |    -|___|   __|   |  _|  _| | | . |  _| | . |   |
|_|_|_|__|__|   |_____|_|_|___|_| |_  |  _|_| |_|___|_|_|
                                  |___|_|                
Tool Name : MK-Encryption
Created BY: Mahmoud Khalid
Profile   : FB/mahmoud.banzema.1

"""
def randomkey():
	key = ''
    	while len(key) != 45:
    		get = random.choice('qwe rtyuiopasdfghjklzxcvbnm0123456789!@#$%^&?')
    	        if get not in key:
    	    		key += get
    	print key
    	key = ''
def help():
	print "1 - Get Random key\n2 - Encryption string\n3 - Unencpryption string\n4 - Clear Screen\n5 - Help\n6 - Exit"
banner()
help()
while True:
	choice = raw_input('\nChoice :  ').lower()
	if choice == '1':
		print "Choice one key for set in a variable words='' in source code script\n"
		for somekey in range(11):
			randomkey()
	if choice == '2':
		encrypted = ''
		string = raw_input('String >').lower()
		for i in range(len(string)):
			encrypted += words[words.index(string[i])+18-45].upper()
		print encrypted
	if choice == '3':
		unencrypted = ''
		unencryptedstring = raw_input('Unencrypted String >').lower()
		for oneunencryptedstring in range(len(unencryptedstring)):
			unencrypted += words[words.index(unencryptedstring[oneunencryptedstring])-18].upper()
		print unencrypted
	if choice == '4':
		call('clear')
	if choice == '5':
		help()
	if choice == '6':
		exit()
	else:
		continue;
