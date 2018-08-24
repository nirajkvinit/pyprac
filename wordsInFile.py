fileReader = open("test.txt", 'r')
linesCount = 0
wordsCount = 0
charactersCount = 0

for line in fileReader:
	wordsCount += len(line.split())
	linesCount += 1
	charactersCount += len(line)

print("Total words: ", wordsCount, "Total Lines: ", linesCount)	
print("Total characters: ", charactersCount)