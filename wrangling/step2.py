# STEP TWO: total mentions per season per character

# before this step, I did a find/replace in Notepad++ 
# searching for '\[.*?\]'' and replacing with '' so any names 
# in action brackets weren't counted

# open the file created in step 1 
# it has the full text of each episode with the speaker 
# in all caps
with open('caps9.txt', encoding = 'utf-8') as f:
	lines = f.readlines()

# initiate a bunch of 0 counters, 1 for each character
# there's 100% a faster/better way to do this, but this works
andycount = 0
erincount = 0
jimcount = 0
pamcount = 0
michaelcount = 0
dwightcount = 0
ryancount = 0
robertcount = 0
jancount = 0
roycount = 0
stanleycount = 0
kevincount = 0
meredithcount = 0
angelacount = 0
oscarcount = 0
phylliscount = 0
kellycount = 0
tobycount = 0
creedcount = 0
darrylcount = 0
hollycount = 0
gabecount = 0
nelliecount = 0
clarkcount = 0
petecount = 0
toddcount = 0
davidcount = 0
karencount = 0
charlescount = 0
jocount = 0
senatorcount = 0
deangelocount = 0
valcount = 0
cathycount = 0
dannycount = 0

# iterate through the words and count names (and commonly 
# used nicknames)  
for line in lines:
	for word in line.split():
		if 'Andy' in word:
			andycount += 1
		if 'Erin' in word:
			erincount += 1
		if 'Jim' in word:
			jimcount += 1
		if 'Pam' in word:
			pamcount += 1
		if 'Mike' in word or 'Michael' in word:
			michaelcount += 1
		if 'Dwight' in word:
			dwightcount += 1
		if 'Ryan' in word:
			ryancount += 1
		if word == 'Robert':
			robertcount += 1
		if 'Jan' in word:
			jancount += 1
		if 'Roy' in word:
			roycount += 1
		if 'Stanley' in word:
			stanleycount += 1
		if 'Kev' in word:
			kevincount += 1
		if 'Meredith' in word:
			meredithcount += 1
		if 'Angela' in word:
			angelacount += 1
		if 'Oscar' in word:
			oscarcount += 1
		if 'Phyl' in word:
			phylliscount += 1
		if 'Kel' in word:
			kellycount += 1
		if 'Toby' in word:
			tobycount += 1
		if 'Creed' in word:
			creedcount += 1
		if 'Darryl' in word:
			darrylcount += 1
		if 'Holly' in word:
			hollycount += 1
		if 'Gabe' in word:
			gabecount += 1
		if 'Nellie' in word:
			nelliecount += 1
		if 'Clark' in word:
			clarkcount += 1
		if 'Pete' in word:
			petecount += 1
		if 'Todd' in word or 'Pack' in word:
			toddcount += 1
		if 'David' in word:
			davidcount += 1
		if 'Karen' in word:
			karencount += 1
		if 'Charles' in word:
			charlescount += 1
		if word == 'Jo':
			jocount += 1
		if 'senator' in word.lower():
			senatorcount += 1
		if 'Deangelo' in word:
			deangelocount += 1
		if word == 'Val':
			valcount += 1
		if 'Cathy' in word or 'Kathy' in word:
			cathycount += 1
		if 'Danny' in word:
			dannycount += 1

# I printed to the command line and piped to results 
# to a new series of files called count1.txt - count9.txt
print('\nAndy' , andycount , '\nErin' , erincount , '\nJim' , jimcount , '\nPam' , pamcount , '\nMichael' , michaelcount , '\nDwight' , dwightcount , '\nRyan' , ryancount , '\nRobert' , robertcount , '\nJan' , jancount , '\nRoy' , roycount , '\nStanley' , stanleycount , '\nKevin' , kevincount , '\nMeredith' , meredithcount , '\nAngela' , angelacount , '\nOscar' , oscarcount , '\nPhyllis' , phylliscount , '\nKelly' , kellycount , '\nToby' , tobycount , '\nCreed' , creedcount , '\nDarryl' , darrylcount , '\nHolly' , hollycount , '\nGabe' , gabecount , '\nNellie' , nelliecount , '\nClark' , clarkcount , '\nPete' , petecount , '\nTodd' , toddcount , '\nDavid' , davidcount , '\nKaren' , karencount , '\nCharles' , charlescount , '\nJo' , jocount , '\nSenator' , senatorcount , '\nDeangelo' , deangelocount , '\nVal' , valcount , '\nCathy' , cathycount , '\nDanny' , dannycount)