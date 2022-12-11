# Program untuk mengkalkulasikan 2 buah binary sepanjang 256-bit secara XOR (bitwise)
import keygenerator

# function untuk mengubah menjadi komplemen
def komplemen(x):
    if x == "1":
        return "0"
    else:
        return "1"

# function operasi tambah
def tambah(x, y):
    if x == "1":
        return "1"
    else:
        if y == "1":
            return "1"
        else:
            return "0"

# function operasi kali
def kali(x,y):
    if x == "1" and y == "1":
        return "1"
    else:
        return "0"

# function untuk mempadding jadi 256 bits
def to256bit(x):
    padded = ""

    for i in range(len(x)-1, -1, -1):
        padded = x[i] + padded
    

    for i in range(256-len(x)):
        padded = "0" + padded
    return padded

# public value
# contoh penggunaan functionnya :
#   p, q = keygenerator.generatePublicVal()
# permisalan
p = 23
q = 5
print("misalkan:")
print(f"p: {p}")
print(f"q: {q}\n")

# private key
# contoh penggunaan functionnya :
#   privatekey1, privatekey2 = keygenerator.generatePrivateKey()
# permisalan
privatekey1 = 10
privatekey2 = 9
print("misalkan:")
print(f"Private key 1: {privatekey1}")
print(f"Private key 2: {privatekey2}\n")

# mencari combined key
combinedkey1, combinedkey2 = keygenerator.getCombinedKey(p, q, privatekey1, privatekey2)
print(f"Combined key 1: {combinedkey1}")
print(f"Combined key 2: {combinedkey2}\n")

# misalkan information kita berupa string
information = "Matdis"
print(f"Information: {information}")

# menampilkan data-data dalam binary
print(" ")
print("Data dalam binary:")

converted_privatekey1 = keygenerator.toBinary(privatekey1)
converted_privatekey2 = keygenerator.toBinary(privatekey2)
print(f"Private key 1: {converted_privatekey1}")
print(f"Private key 2: {converted_privatekey2}\n")

converted_combinedkey1 = keygenerator.toBinary(combinedkey1)
converted_combinedkey2 = keygenerator.toBinary(combinedkey2)
print(f"Combined key 1: {converted_combinedkey1}")
print(f"Combined key 2: {converted_combinedkey2}\n")

converted_information = keygenerator.toBinary(information)
print(f"Information: {converted_information}\n")


# misalkan saja combined key yg dipakai adalah combined key 1
combined_key = converted_combinedkey1

# temp adalah penyimpan informasi sementara, baik yang belum diubah maupun yang sudah diubah
temp = "" 

combined_key = to256bit(combined_key)
information = to256bit(converted_information)

# permisalan combined key 
# combined_key = "1011000000100000100010011101011011000001001010100101000010011100011100111100111000101110010000000001010110101001101101001111100001010000000100001010010111101000010110111100111001001110010111110011001000001011111111100011001101011011101111110011000110101011"
# information = "1011111001010000100110110110110111011011001000010111101111011101110011101011010110101110111000101011011101101000011110010000111111101100111001110111011000100101010000010011000100011000011110010100101110100010010011100000100100001111110100011101001010010010"
# proses dekripsi
for i in range(len(combined_key)):
    a = information[i]
    b = combined_key[i]  

    temp += tambah(kali(a, komplemen(b)), kali(komplemen(a), b))

print(f"Informasi yang telah dienkripsi: {temp}\n")    

changed_information = temp
temp = ""
# proses enkripsi
for i in range(len(combined_key)):
    a = changed_information[i]
    b = combined_key[i]

    temp += tambah(kali(a, komplemen(b)), kali(komplemen(a), b))

print(f"Informasi yang telah didekripsi: {temp}")        