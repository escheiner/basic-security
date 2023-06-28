

def encrypt(text, key):

    encrypted = ""
        
    for letter in text:
        if letter.isupper():
            encrypted += chr((ord(letter) + key-65) % 26 + 65)
        if letter.islower():
            encrypted += chr((ord(letter) + key-97) % 26 + 97)
    return encrypted  


def decrypt(text, key):
    decrypted = ""
        
    for letter in text:
        if letter.isupper():
            decrypted += chr((ord(letter) - key-65) % 26 + 65)
        if letter.islower():
            decrypted += chr((ord(letter) - key-97) % 26 + 97)
    return decrypted   


first_message = encrypt("my name is esty", 5)
print("Encryted = " + first_message)
print("Decrypted = " + decrypt(first_message, 5))
