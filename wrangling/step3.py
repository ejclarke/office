# STEP 3: count how many times a character is mentioned

# before this step, I manually combined all of the caps.txt files
# to create one file with the full text of all seasons
with open('fullshow.txt', encoding = 'utf-8') as f:
	lines = f.readlines()

# initiate an empty list
lst = []
# fill the list with each line in which a character's name appears
for line in lines:
	for word in line.split():
		if "Danny" in word:
			lst.append(line)

counts = dict()
# iterate through the list, counting each time a speaker
# mentions the character we're interested in (speaker names
# end in :)
for i in lst:
	for l in i.split():
		if l.endswith(':'):
			counts[l] = counts.get(l, 0) + 1

# sort and print only the top 10 
# this was dumb and I wish I hadn't done it - 
# just get the whole list and whittle it down in R
t = sorted(counts.items(), key=lambda x:-x[1])[:10]

# append the counts to the end of a mentionagg.txt file
with open('mentionagg.txt', 'a+') as open_file:
	for x in t:
		open_file.write("\nDANNY {0} {1}".format(*x))