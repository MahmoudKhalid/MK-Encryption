import random
from subprocess import call

#================================== [Configure ] ====================================#
words = "2\>*(& .9[%8dy5'u?eqacwimx6r<n)1z+~,l;j@_s#]^/!7v=g$3f-{4kto}ph:b0"            #encryption key 
buffer = 42                                                                             #buffer 42 default Maximum 64
randomkeycreate = "qwe rtyuiopasd:fghjklzxcvbnm01234567\\89~!@#$%^&*()_+-='[]{}?,.<>/;" #Random key create
#====================================================================================#

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
def randomkey(createkey,calc):
        key = ''
        while len(key) != len(createkey):
                get = random.choice(createkey)
                if get not in key:
                        key += get
        print '{} - {}'.format(calc,key)
        key = ''
def help():
        print "1 - Get Random key\n2 - Encryption string\n3 - Unencpryption string\n4 - Clear Screen\n5 - Help\n6 - Exit"
banner()
help()
if buffer > len(randomkeycreate):
        print 'Warning : Maximum buffer {}/{}'.format(len(randomkeycreate),buffer)
else:
        print 'Buffer status {}/{}'.format(len(randomkeycreate),buffer)
while True:
        choice = raw_input('\nChoice :  ').lower()
        if choice == '1':
                calc = 0
                print "Choice one key for set in a variable words='' in source code script\n"
                for somekey in range(10):
                        calc += 1
                        randomkey(randomkeycreate,calc)
        elif choice == '2':
                try:
                        encrypted = ''
                        string = raw_input('String >').lower()
                        for i in range(len(string)):
                                encrypted += words[words.index(string[i])+buffer-len(randomkeycreate)].upper()
                        print encrypted
                except:
                        if buffer > len(randomkeycreate):
                                print "Failed the buffer > {}, Maximum {}".format(buffer,len(randomkeycreate))
                        elif len(words) != len(randomkeycreate):
                                print "Failed please set a new random key to variable word=' '"
                        else:
                                print "Failed please change random key"
        elif choice == '3':
                try:
                        unencrypted = ''
                        unencryptedstring = raw_input('Unencrypted String >').lower()
                        for oneunencryptedstring in range(len(unencryptedstring)):
                                unencrypted += words[words.index(unencryptedstring[oneunencryptedstring])-buffer].upper()
                        print unencrypted
                except:
                        if buffer > len(randomkeycreate):
                                print "Failed the buffer > {}, Maximum {}".format(buffer,len(randomkeycreate))
                        elif len(words) != len(randomkeycreate):
                                print "Failed please set a new random key to variable word=' '"
                        else:
                                print "Failed please change random key"
        elif choice == '4':
                call('clear')
        elif choice == '5':
                help()
        elif choice == '6':
                exit()
        else:
                continue;
