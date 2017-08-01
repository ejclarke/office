# STEP 4: figure out who talks about who

# this is essentially step 2 again
# if I hadn't only printed the head from step 3,
# I could have used that data here, but ¯\_(ツ)_/¯
import sys

with open('fullshow.txt', encoding = 'utf-8') as f:
	lines = f.readlines()
# initiate empty list
michaelsays = []
for line in lines:
	for word in line.split():
		# fill list with the lines spoken by the person in question
		if "DANNY:" in word:
			michaelsays.append(line)

# same as before
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

for line in michaelsays:
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

# make sure you switch back to the original stdout
# I did this to make it easier to print straight to 
# the file without having to edit what I had already 
# done in step 2
orig_stdout = sys.stdout
f = open('speaker.txt', 'a+')
sys.stdout = f
sys.stdout = orig_stdout

# whole big mess - but all you have to do to change the 
# character is find/replace the all-caps names
print('\n DANNY Andy' , andycount , '\n DANNY Erin' , erincount , '\n DANNY Jim' , jimcount , '\n DANNY Pam' , pamcount , '\n DANNY Michael' , michaelcount , '\n DANNY Dwight' , dwightcount , '\n DANNY Ryan' , ryancount , '\n DANNY Robert' , robertcount , '\n DANNY Jan' , jancount , '\n DANNY Roy' , roycount , '\n DANNY Stanley' , stanleycount , '\n DANNY Kevin' , kevincount , '\n DANNY Meredith' , meredithcount , '\n DANNY Angela' , angelacount , '\n DANNY Oscar' , oscarcount , '\n DANNY Phyllis' , phylliscount , '\n DANNY Kelly' , kellycount , '\n DANNY Toby' , tobycount , '\n DANNY Creed' , creedcount , '\n DANNY Darryl' , darrylcount , '\n DANNY Holly' , hollycount , '\n DANNY Gabe' , gabecount , '\n DANNY Nellie' , nelliecount , '\n DANNY Clark' , clarkcount , '\n DANNY Pete' , petecount , '\n DANNY Todd' , toddcount , '\n DANNY David' , davidcount , '\n DANNY Karen' , karencount , '\n DANNY Charles' , charlescount , '\n DANNY Jo' , jocount , '\n DANNY Senator' , senatorcount , '\n DANNY Deangelo' , deangelocount , '\n DANNY Val' , valcount , '\n DANNY Cathy' , cathycount , '\n DANNY Danny' , dannycount)