#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()     #getting input from a user of wethert they want to encrypt or decrypt a message
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".') #if the user does not type  in "encrypt" or "e" or "decrypt" or "d", return zero

def getMessage():
    print('Enter your message: ')
    return input() #getting the message that they want to encryot

def getKey():
    key = 0 #declaring key integer by how much they wanna shift it
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input()) #forcces key given to integer format
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key #getting the key and if they enter a key that is too big or small returning the key value

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = '' #creating code for special cases for example space does not have a character

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS): #the shift starts happening here depending on length of SYMBOL list
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode() #these are the call functions
message = getMessage()
key = getKey()
print('Your translated text is: ') #print statements
print(getTranslatedMessage(mode, message, key))