import re

characters = ""
with open("level4.dat") as f:
    for line in f:
        characters += line

for s in re.findall("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]", characters):
    print s[(len(s)+1)/2-1]
