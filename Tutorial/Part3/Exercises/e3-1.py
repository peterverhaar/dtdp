
import re

poems = open("Shelley.txt" , encoding='utf-8')
lines = []


for line in poems:
    lines.append(line)


for line in lines:
    if re.search( r"\bfire\b" , line , re.IGNORECASE ):
        print(line)


# Using the same text, print all the lines containing either the word "sun" or to word "moon". Use a single regular expression to identify these lines.

# In[2]:


for line in lines:
    if re.search( r'\bsun\b|\bmoon\b' , line ):
        print( line )


# Find all the lines which contain either the singular or the plural form of "star".

# In[3]:


for line in lines:
    if re.search( r'\bstars?\b' , line ):
        print( line )


# Find all the lines which contain either the singular or the plural form of "leaf".

# In[4]:


for line in lines:
    if re.search( r'\blea(f|ves)\b' , line ):
        print( line )


# Find all the lines which contain a word ending in in "ly".

# In[9]:


for line in lines:
    if re.search( r'ly\b' , line ):
        print( line )


# Find all the lines which contain a question mark.

# In[5]:


for line in lines:
    if re.search( r'\?' , line ):
        print( line )


# Find all the lines ending in the character sequence "ain".

# In[6]:


for line in lines:
    if re.search( r'ain$' , line ):
        print( line )


# Find all the lines which contain at least two words that begin with "br"

# In[8]:


for line in lines:
    if re.search( r'\bbr.+\bbr.*' , line ):
        print( line )


# # Exercise 3.3
#
# Download the following file: https://raw.githubusercontent.com/peterverhaar/dtdp/master/Texts/Ulysses.txt. It is the full text of James Joyce's novel Ulysses. Find all the text fragments containing a year (e.g. the sentence “What reflection concerning the irregular sequence of dates 1884, 1885, 1886, 1888, 1892, 1893, 1904 did Bloom make before their arrival at their destination?”)
#

# In[2]:


import re

novel = open("Ulysses.txt" , encoding='utf-8')
lines = []


for line in novel:
    lines.append(line)


# Find fragments in which Joyce chose the dramatic form, or, more specifically, lines which begin with the name of a speaker in capitals, followed directly by a colon.

# In[11]:


for line in lines:
    if re.search( r'\d{4}' , line ):
        print( line )


# Find lines that consist of less than 30 characters. N.B. Use a regular expression, instead of the finction len()

# In[15]:


for line in lines:
    if re.search( r'^.{1,29}$' , line ):
        print(line.strip())


# Find fragments containing words that begin with "O'", followed by an apostrophe (e.g. O'Connell, O'Brian)

# In[17]:


for line in lines:
    if re.search( r'\b[Oo]\'[A-Z]' , line ):
        print(line)


# Find fragments in which Joyce chose the dramatic form, or, more specifically, lines which begin with the name of a speaker in capitals, followed directly by a colon.

# In[19]:


for line in lines:
    if re.search( r'[A-Z]+:' , line ):
        print(line)


# # Exercise 3.4
#
# The file “bibliography.txt”, which you can download from https://raw.githubusercontent.com/peterverhaar/dtdp/master/Texts/bibliography.txt, contains a list of articles, formatted according to the APA citation style. For each title, try to extract the year of publication, the title and the name of the journal.
#

# In[5]:


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


# # Exercise 3.5
#
# The file "stcn.txt" (https://raw.githubusercontent.com/peterverhaar/dtdp/master/Texts/stcn.txt) is a small export from the Short Title Catalogue of the Netherlands. It offers information on 50 titles printed by members of the Elzevier family. Try to convert the export as it is given in the original file to a CSV file. A CSV is file format in which all the values are separated by a comma. The new CSV file should contain the following values: BOOK_ID, full name of the author, year, format and the full title. The full name of the author must be given as follows: ‘First name + SPACE + Last name’.
# The CSV file must start with a header which specifies names for all the columns. The output file should be named ‘data.csv’.
#

# In[3]:


import re

stcn = open( 'stcn.txt' )
out = open( 'data.csv' , 'w' )

data = dict()

## print the header
out.write( 'BOOK_ID,fullName,year,format,title\n' )

for line in stcn:
    print(line)
    if re.search( r'^RECORD' , line ) and len(data) > 0:

        ## remove commas
        for value in data:
            data[value] = re.sub( ',' , '' , data[value] )

        ## Create variable fullName, using the first and the last name
        fullName = data.get('first' , '')
        if re.search( '\w' , fullName ):
            fullName += ' '
        fullName += data.get('last' , '')

        ## write the data to a CSV file
        out.write('{},{},{},{},{}\n'.format( data.get('book_id' , '') , fullName , data.get('year' , '') , data.get('format' , '') , data.get('title' , '') )  )

        ## remove all values from the data dictionary
        data.clear()

    elif re.search( r'^YEAR' , line ):
        line = re.sub( 'YEAR: ' , '' , line )
        data['year'] = line.strip()
    elif re.search( r'^FORMAT' , line ):
        line = re.sub( 'FORMAT: ' , '' , line )
        data['format'] = line.strip()
    elif re.search( r'^TITLE' , line ):
        line = re.sub( 'TITLE: ' , '' , line )
        data['title'] = line.strip()
    elif re.search( r'^B_ID' , line ):
        line = re.sub( 'B_ID: ' , '' , line )
        data['book_id'] = line.strip()
    elif re.search( r'^B_ID' , line ):
        line = re.sub( 'B_ID: ' , '' , line )
        data['book_id'] = line.strip()
    elif re.search( r'^NAME_LAST' , line ):
        line = re.sub( 'NAME_LAST: ' , '' , line )
        data['last'] = line.strip()
    elif re.search( r'^NAME_FIRST' , line ):
        line = re.sub( 'NAME_FIRST: ' , '' , line )
        data['first'] = line.strip()

## print the vary last record

if len(data) > 0:

    ## remove commas
    for value in data:
        data[value] = re.sub( ',' , '' , data[value] )

    fullName = data.get('first' , '')
    if re.search( '\w' , fullName ):
        fullName += ' '
    fullName += data.get('last' , '')

    out.write('{},{},{},{},{}\n'.format( data.get('book_id' , '') , fullName , data.get('year' , '') , data.get('format' , '') , data.get('title' , '') )  )

out.close()


# In[ ]:
