# Name: easypeasy
## Platform: picoCTF
## Time elapsed: 5hrs
## Category: Cryptography

Despite the name of the challenge, it only has a 19% clear rate, so not exactly a walk in the park.

We're first presented with an encrypted version of our flag which is 64 symbols long, but the flag itself is not 64 symbols long as we will shortly see

1. First I had to de-mystify this line

result = list(map(lambda p, k: "{:02x}".format(ord(p)^k), flag, key))

which basically equates to 
take item 0 of flag file and xor it with item 0 of key file
take item 1 of flag file and xor it with item 1 of key file
and it does this for all the items until the flag file reaches the end of the characters it contains
all of this is then presented as an 2 symbol (8-bit) hex number which is indicated by "{:02x}" That means that the flag contains 32 symbols since each character that is passed in this encrpytion spits out a 2 symbol hex. (64 symbols / 2 = 32)

2. If we encrypt the letter a and then without exiting the script we try to encrypt the letter a again, we will get 2 different values, this is because the key value changes every time we pass something to the script. This is because every time we encrypt something the key location sets its beginning to +1 of our last used key location in the key file.
For example
lets say our key is abcdefg. The current beginning of the key is 0 which corresponds to a. If we encrypt 123, this will use a to encrypt 1, b to encrypt 2 and c to encrypt 3. Now the script will automatically set the new beginning of the key to be at 3 which corresponds to d.

3. So at this point I noticed that KEY_LEN = 50000 and in the encrypt function if stop >= KEY_LEN:, then stop = stop % KEY_LEN. Since the startup function has a 0 passed in to its key_location variable, maybe if we set managed to get stop to exactly 50000 then the new stop would be 0 and we could maybe replicate the flag. So I generated a padding file that has 50000 characters and I tried pasting that in to the encryption field, but that didn't work because at the time I didn't know pythons input function has a 4095 symbol limit.

So then since we want 50000 to reach characters we will have to paste in a padding of 4095 characters 12 times, then since the initial flag encryption already used up 32 characters, we add that and we get 49172, 50000-49172 = 828, so we'll have 2 types of padding. padding 1 will be 4095 characters long and padding 2 will be 828 characters long. This will ensure that when we encrypt our padding1 12 times and our padding2 1 time that we have looped back to our initial starting point of key_location = 0

4. At this point you could brute force it the characters one by one, however that would take some time. So instead we will pass in 32 of an arbitrarily chosen ascii value and note down what the encryption of our ascii value is. In my case I chose the value 0 which is 0x30 or d'48.
Since we know that the encrpytion xors every single value with the key, and since we know the input (0) and the output (encrypted msg) we xor the encrypted message and the input(32 zeros) to obtain the first 32 key values. This works because the inverse of a Xor function is another xor function. Now since we know the first 32 key values, we xor the encrypted flag with the first 32 key values and we get our flag!
