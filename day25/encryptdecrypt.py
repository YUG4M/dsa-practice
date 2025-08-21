a= "Bomb has been planted"
encryptlog= ""
decrypt=""

for i in a:
    asciivalue= ord(i)
    asciivalue+= int(5)
    encryptlog+=chr(asciivalue)

print(encryptlog)

for j in encryptlog:
    ascval= ord(j)
    ascval-= int(5)
    decrypt+= chr(ascval)

print(decrypt)