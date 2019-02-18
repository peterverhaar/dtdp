
# # Exercise 3.4
#
# The file “bibliography.txt”, which you can download from https://raw.githubusercontent.com/peterverhaar/dtdp/master/Texts/bibliography.txt, contains a list of articles, formatted according to the APA citation style. For each title, try to extract the year of publication, the title and the name of the journal.
#



import re

file = open(  "bibliography.txt" )

for pub in file:
    match = re.search( r'\((\d+)\)' , pub )
    if match:
        year = match.group(1)

    match = re.search( r'\"(.+)\"' , pub )
    if match:
        title = match.group(1)

    match = re.search( r'\".+\"\s([A-Za-z\s]*)\d' , pub )
    if match:
        journal = match.group(1)

    print( year + '\n' +  title + '\n' + journal + '\n')
