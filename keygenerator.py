# program untuk mengenerate key
import math
import random

# function untuk mengconvert string ke dalam bentuk binary
def toBinary(a):
    temp = str(a)
    tempbin = []
    textAsBinary = ""

    for i in temp:
        tempbin.append(ord(i))
        
    for i in tempbin:
        textAsBinary += str(bin(i)[2:])

    return textAsBinary

# function untuk mengenerate key random
def generatePublicVal():
    # max value dari 256 bits
    max_value = math.pow(2, 256) - 1

    # random untuk keynya
    temp = random.randint(0, max_value)
    temp2 = random.randint(0, max_value)

    # generate key ke 2 yang relatif prima ke key pertama
    while euclidean(temp, temp2) != 1:
        temp2 = random.randint(0, max_value)

    return temp, temp2

def generatePrivateKey():
    # max value dari 256 bits
    max_value = math.pow(2, 256) - 1

    # random untuk keynya
    temp = random.randint(0, max_value)
    temp2 = random.randint(0, max_value)

    return temp, temp2

def euclidean(m, n):
    while n != 0:
        r = m % n
        m = n
        n = r
    
    return m

def getCombinedKey(public1, public2, private1, private2):
    publickey1 = math.pow(public2, private1) % public1
    publickey2 = math.pow(public2, private2) % public1

    combinedKey1 = math.pow(publickey2, private1) % public1
    combinedKey2 = math.pow(publickey1, private2) % public1

    return int(combinedKey1), int(combinedKey2)