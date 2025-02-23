
# Caesar Cipher

MAX_KEY_SIZE = 26

def getMode():

	while True:

		print('Do you wish to encrypt, decrypt or brute force a message?')
		mode = input().lower()

		if mode in 'encrypt e decrypt d brute b'.split():

			return mode

		else:

			print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b".')


def getMessage():

	print('Enter your message: ')
	return input()


def getKey():

	key = 0

	while True:

		print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
		key = int(input())

		if (key >= 1 and key <= MAX_KEY_SIZE):

			return key


def getTranslatedMessage(mode, message, key):

	if mode[0] == 'd':

		key = -key

	translated = ''

	for symbol in message:

		if symbol.isalpha():

			num = ord(symbol)
			num = num + key

			if symbol.isupper():

				if num > ord('Z'):

					num = num - 26

				elif num < ord('A'):

					num = num + 26

			elif symbol.islower():

				if num > ord('z'):

					num = num - 26

				elif num < ord('a'):

					num = num + 26


			translated = translated + chr(num)

		else:

			translated = translated + symbol


	return translated


mode = getMode()
message = getMessage()

if mode[0] != 'b':

	key = getKey()


print('Your translated text is: ')

if mode[0] != 'b':

	print(getTranslatedMessage(mode, message, key))

else:

	for key in range(1, MAX_KEY_SIZE + 1):

		print(key, getTranslatedMessage('decrypt', message, key))


