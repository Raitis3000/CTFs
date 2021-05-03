#!/usr/bin/python3 -u
import os.path

KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"


def startup(key_location):
	print("startup")
	flag = open(FLAG_FILE).read()
	kf = open(KEY_FILE, "r").read()

	start = key_location	# 0
	stop = key_location + len(flag)

	key = kf[start:stop]
	key_location = stop # 0 + len(flag)
	
	if start == 0:
		print(key)
	
	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ ord(k)), flag, key))
	
	#lambda p, k: "{:02x}".format(ord(p) ^ k)
	# 
	print("This is the encrypted flag!\n{}\n".format("".join(result)))

	return key_location

def encrypt(key_location):
	print("Encrypt")
	ui = input("What data would you like to encrypt? ").rstrip() #can't input more than 4095 characters
	if len(ui) == 0 or len(ui) > KEY_LEN:
		return -1
	print("key location: {}".format(key_location))
	start = key_location # start = len(flag)
	stop = key_location + len(ui)	#stop = len(flag) + length of user input
	
	kf = open(KEY_FILE, "rb").read()
	print("Stop before if statement: {}".format(stop))
	if stop >= KEY_LEN:
		print("stop>=KEY_LEN")
		stop = stop % KEY_LEN
		print("new stop value: {}".format(stop))			# need to get key_location = 0
		key = kf[start:] + kf[:stop]
		print("start: and :stop: {} {}".format(start,stop))
	else:
		key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

	print("Here ya go!\n{}\n".format("".join(result)))

	return key_location


print("******************Welcome to our OTP implementation!******************")
c = startup(0)
while c >= 0:
	c = encrypt(c)
	
	
	
	#5b 1e 56 4b 6e 41 5c 0e 39 4e 04 01 38 4b 08 55 3a 4e 5c 59 7b 6d 4a 5c 5a 68 4d 50 01 3d 6e 4b          encrypted flag
	
	#
