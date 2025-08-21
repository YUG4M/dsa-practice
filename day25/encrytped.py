import random

a= "Bomb has been planted!!!"
encryptlog= ""
decrypt=[]
code=0

for i in a:
    asciivalue= ord(i)
    code+= random.randint(1,10)
    decrypt.append(code)
    asciivalue+=code
    encryptlog+=chr(asciivalue)

print(encryptlog)

decode=""
for j in range(len(encryptlog)):
    asciivalue = ord(encryptlog[j])  
    asciivalue-= decrypt[j]
    decode += chr(asciivalue)

print(decode)