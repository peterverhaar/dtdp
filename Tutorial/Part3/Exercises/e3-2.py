
# Using the same text, print all the lines containing either the word "sun" or to word "moon". Use a single regular expression to identify these lines.

for line in lines:
    if re.search( r'\bsun\b|\bmoon\b' , line ):
        print( line )


# Find all the lines which contain either the singular or the plural form of "star".


for line in lines:
    if re.search( r'\bstars?\b' , line ):
        print( line )


# Find all the lines which contain either the singular or the plural form of "leaf".



for line in lines:
    if re.search( r'\blea(f|ves)\b' , line ):
        print( line )


# Find all the lines which contain a word ending in in "ly".


for line in lines:
    if re.search( r'ly\b' , line ):
        print( line )


# Find all the lines which contain a question mark.


for line in lines:
    if re.search( r'\?' , line ):
        print( line )


# Find all the lines ending in the character sequence "ain".

for line in lines:
    if re.search( r'ain$' , line ):
        print( line )


# Find all the lines which contain at least two words that begin with "br"



for line in lines:
    if re.search( r'\bbr.+\bbr.*' , line ):
        print( line )
