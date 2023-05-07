def anagramChecker(word, another_word):
	if len(word) != len(another_word):
		return False
	else:
		list1 = []
		for letter in word:
			list1.append(letter)

		list2 = []
		for letter in another_word:
			list2.append(letter)

		list1.sort()
		list2.sort()

		for x in range(len(list1)):
			if list1[x] != list2[x]:
				return False
		else:
			return True

def noDuplicate(listword):
	dupList = []
	for word in listword:
		dupList.append(word)
	for word in listword:
		dupList.remove(word)
		if word in dupList:
			return False
	else:
		return True

def ana(listword):
	for x in range(len(listword)):
		if x != len(listword) - 1:
			combinedList = listword[:x] + listword[x+1:]
			for word in combinedList:
				if (anagramChecker(listword[x], word)):
					return False
		elif x == len(listword) - 1:
			combinedList = listword[:x]
			for word in combinedList:
				if (anagramChecker(listword[x], word)):
					return False
	else:
		return True

with open('day4input.txt', 'r') as fileopen:
	linesarray = fileopen.readlines()

total_correct = 0

for line in linesarray:
	line = line.rstrip()
	listword = line.split(' ')
	if noDuplicate(listword) and ana(listword):
		print(f"{listword}")
		total_correct += 1

print(total_correct)
	