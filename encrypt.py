import random


class Hash:


    def randomizer(self):
        return self.salt

    def __init__(self, keys):
        self.lower_characters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a',
                                 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
        self.upper_characters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A',
                                 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
        self.numbers_characters = ['1', '2', '3',
                                   '4', '5', '6', '7', '8', '9', '0']
        self.special_chars = ['!', '@', '#', '$', '%', '^', '&',
                              '*', '(', ')', '-', '_', '+', '=', ',', ' ', ';', ':']
        self.reference_characters = self.lower_characters + \
            self.upper_characters + self.numbers_characters + self.special_chars
        self.combined = ['a', 'x', 'T', 'F', 'B', '8', '*', ';', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'w', 'z', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'e', 'R', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'r', 'D',
                         'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 't', 'V', 'N', 'M', '1', '2', '3', '4', '5', '6', 'y', '7', '9', '0', '!', '@', '#', '$', '%', '^', 'u', '&', '(', ')', '-', '_', '+', '=', ',', 'i', ' ', ':', 'o', 'q']

        # Generates a float from the key which will be used to randomize all characters, numbers and special symbols
        self.salt = ''
        for key in keys:
            self.salt = self.salt + str(self.combined.index(key))
        self.salt = int(self.salt)/10**len(self.salt)

        # Uses a float generated from the key to randomize the characters
        random.shuffle(self.reference_characters, self.randomizer)

    def encrypt(self, message):
        encrypted_message = ''
        for message_character in message:
            target = self.reference_characters.index(message_character)
            encrypted_message = encrypted_message + self.combined[target]
        return encrypted_message

    def decrypt(self, message):
        decrypted_message = ''
        for encrypted_message_character in message:
            target = self.combined.index(encrypted_message_character)
            decrypted_message = decrypted_message + \
                self.reference_characters[target]
        return decrypted_message

# http://www.trytoprogram.com/c-examples/c-program-to-encrypt-and-decrypt-string/s