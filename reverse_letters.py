def reverse_letters(word):
	index = 0
	reversed_word = ''
	while index < len(word):
		reversed_word = word[index] + reversed_word
		index = index + 1

	print(reversed_word)

reverse_letters('apple')

def reverse2(word):
	for letter in word:
		print(letter)

reverse2('test')
