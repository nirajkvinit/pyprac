sentence = input()
sentence = sentence + " "
word = ""
for letter in sentence:	
	if letter.isalpha():		
		word += letter
	else:		
		first_letter = word[:1].lower()
		if first_letter >= "h":
			print(word.upper())
		
		word = ""