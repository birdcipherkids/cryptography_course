# Detect English Module

# To use, type this code:
# import detectEnglish

# detectEnglish.isEnglish(some string) - returns True or False
# Note: There must be a 'dictionary.txt' file in this directory with all english words in it, one word per line.


UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'


def loadDictionary():

	dictionaryFile = open('dictionary.txt')
	englishWords = {}

	for word in dictionaryFile.read().split('\n'):

		englishWords[word] = None
	
	dictionaryFile.close()
	return englishWords


ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):

	global ENGLISH_WORDS

	message = message.upper()
	message = removeNonLetters(message)
	possibleWords = message.split()

	if possibleWords == []:

		return 0.0

	matches = 0

	for word in possibleWords:

		if word in ENGLISH_WORDS:

			matches = matches + 1

	return float(matches) / len(possibleWords)


def removeNonLetters(message):

	lettersOnly = []

	for symbol in message:

		if symbol in LETTERS_AND_SPACE:

			lettersOnly.append(symbol)

	return ''.join(lettersOnly)


def isEnglish(message, wordPercentage=40, letterPercentage=85):

	wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
	numLetters = len(removeNonLetters(message))
	messageLettersPercentage = float(numLetters) / len(message) * 100
	lettersMatch = messageLettersPercentage >= letterPercentage

	return wordsMatch and lettersMatch


#message_user = input('Enter your message: ')

#removeNonLetters(message_user)
#print(ENGLISH_WORDS)
#getEnglishCount(message_user)
#print(isEnglish(message_user))


