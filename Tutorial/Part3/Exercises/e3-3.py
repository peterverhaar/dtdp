
# # Exercise 3.3
#
# Download the following file: https://raw.githubusercontent.com/peterverhaar/dtdp/master/Texts/Ulysses.txt. It is the full text of James Joyce's novel Ulysses. Find all the text fragments containing a year (e.g. the sentence “What reflection concerning the irregular sequence of dates 1884, 1885, 1886, 1888, 1892, 1893, 1904 did Bloom make before their arrival at their destination?”)
#


import re

novel = open("Ulysses.txt" , encoding='utf-8')
lines = []


for line in novel:
    lines.append(line)


# Find fragments in which Joyce chose the dramatic form, or, more specifically, lines which begin with the name of a speaker in capitals, followed directly by a colon.


for line in lines:
    if re.search( r'\d{4}' , line ):
        print( line )


# Find lines that consist of less than 30 characters. N.B. Use a regular expression, instead of the finction len()


for line in lines:
    if re.search( r'^.{1,29}$' , line ):
        print(line.strip())


# Find fragments containing words that begin with "O'", followed by an apostrophe (e.g. O'Connell, O'Brian)



for line in lines:
    if re.search( r'\b[Oo]\'[A-Z]' , line ):
        print(line)


# Find fragments in which Joyce chose the dramatic form, or, more specifically, lines which begin with the name of a speaker in capitals, followed directly by a colon.

for line in lines:
    if re.search( r'[A-Z]+:' , line ):
        print(line)
