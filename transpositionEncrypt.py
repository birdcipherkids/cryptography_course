# Transposition encrypt

import pyperclip

def main():

	myMessage = input('Enter the message to encrypt: ')
	myKey = 8

	cipherText = encryptMessage(myKey, myMessage)

	print(cipherText + '|')
	pyperclip.copy(cipherText)


def encryptMessage(key, message):

	cipherText = [''] * key

	for col in range(key):

		pointer = col

		while pointer < len(message):

			cipherText[col] = cipherText[col] + message[pointer]
			pointer = pointer + key
			


	return ''.join(cipherText)



if __name__ == '__main__':

	main()