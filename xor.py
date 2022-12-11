# Program untuk mengkalkulasikan 2 buah binary sepanjang 256-bit secara XOR (bitwise)

combined_key = input("Combined key: ")
print("")
information = input("Information: ")
print("")
temp = "" # temp adalah penyimpan informasi sementara, baik yang belum diubah maupun yang sudah diubah

# proses dekripsi
for i in range(len(combined_key)):
    if combined_key[i] == information[i]:
        temp += "0"
    else:
        temp += "1"

print(f"Informasi yang telah dienkripsi: {temp}\n")    

changed_information = temp
temp = ""
# proses enkripsi
for i in range(len(combined_key)):
    if combined_key[i] == changed_information[i]:
        temp += "0"
    else:
        temp += "1"

print(f"Informasi yang telah didekripsi: {temp}")        