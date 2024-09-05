import random
from random import shuffle

Key      = "BLae30WQUVZy1p4zbCu7r2TSsldnRINxHYt5 wDJEcvA6hGik8ogPMFjXO9qfmK"
Sequence = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 '

def shuffle_word(word): # Use this function to generate a new key for the sequence
    word = list(word)
    shuffle(word)
    return ''.join(word)


def Encrypt(message):
    result = ""
    for words in range(len(message)):
        if message[words] == " ":
            result += " "
        else:
            for i in range(62):
                if Sequence[i] == message[words]:
                    result += Key[i]
        
    return result

def Decrypt(message):
    result = ""
    for words in range(len(message)):
        if message[words] == " ":
            result += " "
        else:
            for i in range(62):
                if Key[i] == message[words]:
                    result += Sequence[i]
    return result