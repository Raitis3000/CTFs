import os
import sys
import fileinput
removeme = "What data would you like to encrypt? Here ya go!"
for line in fileinput.input("results.txt", inplace=1):
	sys.stdout.write(line.replace("What data would you like to encrypt? Here ya go!", ''))
