from encrypt import Hash

message = "The quick brown fox jumped over the"
hash = Hash("2898")
encrypted_message = hash.encrypt(message)
decrypted_message = hash.decrypt(encrypted_message)
print(encrypted_message)
print(decrypted_message)