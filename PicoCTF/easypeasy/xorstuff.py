#when I entered 32 a's this is what I got
#xor key with a  03 46 07 1d 3d 19 04 59 3d 19 03 57 3d 19 50 03 3d 19 58 59 2a 3d 19 05 59 3d 19 00 57 3f 3d 19
#in dec          3 70 7 29 61 25 4 89 61 25 3 87 61 25 80 3 61 25 88 89 42 61 25 5 89 61 25 0 87 63 61 25

# enc msg     5b 1e 56 4b 6e 41 5c 0e 39 4e 04 01 38 4b 08 55 3a 4e 5c 59 7b 6d 4a 5c 5a 68 4d 50 01 3d 6e 4b
#in dec       91 30 86 75 110 65 92 14 57 78 4 1 56 75 8 85 58 78 92 89 123 109 74 92 90 104 77 80 1 61 110 75
encMsg = [91, 30,  86, 75, 110, 65, 92,  14,  57, 78,  4,   1, 56, 75,  8, 85,  58, 78, 92, 89, 123, 109,  74, 92,  90, 104, 77, 80,   1, 61, 110, 75]
result = [ 3, 70, 7, 29, 61, 25, 4, 89, 61, 25, 3, 87, 61, 25, 80, 3, 61, 25, 88, 89, 42, 61, 25, 5, 89, 61, 25, 0, 87, 63, 61, 25]

i = 0;
u = 0;
a = 97;

key = [];


while i < len(result):
	keystr = result[i] ^ a
	key.append(keystr)
	i += 1

while u < len(encMsg):
	dMsg = key[u] ^ encMsg[u]
	print(chr(dMsg), end='') #PLEASE LET THIS WORK
	u += 1
	

