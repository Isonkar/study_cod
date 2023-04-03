source_file = input()
encryption_key = input() 
file_for_encryption = input() 
decryption_file = input()

encr_dict = {}
decryp_dict = {}
result_encryption = []
result_decryption = []

for i in range(len(source_file)):
    encr_dict[source_file[i]] = encryption_key[i]

for i in range(len(encryption_key)):
    decryp_dict[encryption_key[i]] = source_file[i]

# до этой строки код работает, словарь с парой ключ - значение создается

for i in range(len(file_for_encryption)):
    if file_for_encryption[i] in encr_dict:
        result_encryption.append(encr_dict[file_for_encryption[i]])
    else:
        result_encryption.append(file_for_encryption[i])

for i in range(len(decryption_file)):
    if decryption_file[i] in decryp_dict:
        result_decryption.append(decryp_dict[decryption_file[i]])
    else:
        result_decryption.append(decryption_file[i])

print(*result_encryption, sep='')
print(*result_decryption, sep='')
