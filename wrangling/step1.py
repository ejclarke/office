# STEP ONE: convert speaker names to all caps

# each season's full text is accessed from a separate file
# the file is formatted so that each line of dialogue is on a separate line
with open('season9.txt', encoding = 'utf-8') as f:
	lines = f.readlines()

# create an empty list for appending lines
lst = []
# iterate through the words in the file
for line in lines:
	for word in line.split():
		# words ending with : are a speaker
		if word.endswith(':'):
			# create a new line, all caps the speaker's name for easier searching later
			word = "\n" + word.upper()
			# reappend the word
			lst.append(word)
		else:
			lst.append(word)

# write to a separate file
# everything is the same except the speaker's name is in all caps
with open('caps9.txt', 'w') as write_file:
	print(' '.join(lst), file = write_file)