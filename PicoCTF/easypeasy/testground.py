import os.path

KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"
#01100001 xor       |a  |0x61
#00110001 	    |1  |0x31
#01010000 #becomes |P  0x50

#flag = open(FLAG_FILE).read() # reads flag file
#kf = open(KEY_FILE, "rb").read() # reads key file as binary

#start = 0 #key starts at the start of the file
#stop = len(flag) #length of the flag file

#key = kf[start:stop]	#key value as an array
#print(key)
#key_location = stop	#length of the key + 1 for terminator

#print("key location: {}".format(key_location))

# {:02x} convert to 2 symbol hex format

result1 = lambda p, k: "{:02x}".format(p^k)
result2 = list(map(lambda p, k: "{:02x}".format(ord(p)^k), flag, key))

print("result2: {}".format(result2))
print("This is the encrypted flag! {} \n".format("".join(result2)))

#result3 = list(map(lambda p, k: "{:02x}".format(p^k), [0x5b], key))
#print("result3: {}".format(result3))
#print("This is the encrypted flag!\n{}\n".format("".join(result3)))

#print(result3)
#5b 1e 56 4b 6e 41 5c 0e 39 4e 04 01 38 4b 08 55 3a 4e 5c 59 7b 6d 4a 5c 5a 68 4d 50 01 3d 6e 4b          encrypted flag
#5b1e564b6e415c0e394e0401384b08553a4e5c597b6d4a5c5a684d50013d6e4b 64/2 = 32 - 1 for null term = 31 long
#0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#0000000000000000


#python input limit = 4095
# * 12 = 49140
# + 32 = 49172
#still need 843 symbols
#each input = 1
#each flag symbol = 1

#key a f

#^ XOR
#01
#10
#=
#11

#11
#10
#=
#01
