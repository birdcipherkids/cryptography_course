# Transposition file cipher

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():

	inputFileName = 'TestDocument.encrypted.txt'
	outputFileName = 'TestDocument2.txt'
	myKey = 10
	myMode = 'decrypt'

	if not os.path.exists(inputFileName):

		print('The file %s does not exists. Quitting....' % (inputFileName))
		sys.exit()


	if os.path.exists(inputFileName):

		print('This will overwrite the file %s. (C)ontinue or (Q)uit' % (outputFileName))
		response = input('> ')

		if not response.lower().startswith('c'):

			sys.exit()


	fileObj = open(inputFileName)
	content = fileObj.read()
	fileObj.close()

	print('%sing...' % (myMode.title()))
	startTime = time.time()

	if myMode == 'encrypt':

		translated = transpositionEncrypt.encryptMessage(myKey, content)

	elif myMode == 'decrypt':

		translated = transpositionDecrypt.decryptMessage(myKey, content)

	totalTime = round(time.time() - startTime, 5)
	print('%sion time: %s seconds' % (myMode.title(), totalTime))

	outputFileObj = open(outputFileName, 'w')
	outputFileObj.write(translated)
	outputFileObj.close()

	print('Done %sing %s (%s characters).' % (myMode, inputFileName, len(content)))
	print('%sed file is %s' % (myMode.title(), outputFileName))


if __name__== '__main__':

	main()

