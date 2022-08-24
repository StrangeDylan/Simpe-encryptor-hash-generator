import random

def genkey(numofbytes: int):
    key = ''
    for i in range(numofbytes):
        piece = hex(random.randint(0, 255))
        if len(piece) < 4: piece = piece[0:2]+'0'+piece[2:3]
        key += piece[2:4]
    return key

def encrypt(text, key):
    counter = 0
    result = ''
    for byte in text:
        byte = ord(byte)
        while counter != len(key):
            byte = byte ^ int(key[counter:counter+2], base=16)
            counter += 2
        counter = 0
        byte = hex(byte)
        if len(byte) % 2 == 1:
            byte = byte[0:2]+'0'+byte[2:len(byte)]
        result += byte[2:len(byte)]
    return result

def decrypt(text, key):
    keycounter = len(key)
    counter = 0
    result = ''
    while counter != len(text):
        textpiece = int(text[counter:counter+2], base=16)
        while keycounter != 0:
            textpiece = textpiece ^ int(key[keycounter-2:keycounter], base=16)
            keycounter -= 2
        result += chr(textpiece)
        keycounter = len(key)
        counter += 2
    return result