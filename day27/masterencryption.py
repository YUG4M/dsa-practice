import random

a = "Bomb has been planted!!!"
encryptlog = ""
decrypt = []
code = 0

for i in a:
    asciivalue = ord(i)
    c = random.randint(1, 10)
    code += c
    decrypt.append(c)
    asciivalue += code
    encryptlog += chr(asciivalue)

print("Encrypted message:", encryptlog)

encrypted_msg = encryptlog
decrypted_msg = ""
code = 0

for j in range(len(encrypted_msg)):
    code += decrypt[j]
    ascii_val = ord(encrypted_msg[j])
    ascii_val -= code
    decrypted_msg += chr(ascii_val)

print("Decrypted message:", decrypted_msg)

choice = input("Did you get the msg (yes/no): ")
if choice == "yes":
    print("Bomb Defused!!!")
else:
    print("Failure")
