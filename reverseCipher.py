# reverse cipher

def reverseCipher(plaintext):

	ciphertext = ''

	i = len(plaintext) - 1

	while i >=0:

		ciphertext = ciphertext + plaintext[i]
		i = i - 1

	return ciphertext

plaintext = 'If you want to keep a secret, you must hide it from yourself'
ciphertext2 = reverseCipher(plaintext)
print(ciphertext2)

