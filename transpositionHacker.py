# Transposition Cipher Hacker

import pyperclip, detectEnglish, transpositionDecrypt

def main():

	myMessage = input('Enter the message to hack: ')

	hackedMessage = hackTransposition(myMessage)

	if hackedMessage == None:

		print('Failed to hack encryption')

	else:

		print('Copying hacked message to clipboard:')
		print(hackedMessage)
		pyperclip.copy(hackedMessage)


def hackTransposition(message):

	print('Hacking....')
	print()
	print('Press Ctrl-C or Ctrl-D to quit at any time')

	for key in range(1, len(message)):

		print('Trying key #%s...' % (key))

		decryptedText = transpositionDecrypt.decryptMessage(key, message)

		if detectEnglish.isEnglish(decryptedText):

			print()
			print('Possible encryption hack: ')
			print('Key %s: %s' % (key, decryptedText[:100]))
			print()
			print('Enter D for done, or just press Enter to continue hacking:')
			response = input('> ')

			if response.strip().upper().startswith('D'):

				return decryptedText


	return None


if __name__=='__main__':

	main()
