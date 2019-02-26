
import re

text = open( '98-0.txt' )
out = open( 'out.txt' , 'w' )

flag = False

for line in text:

    if re.search( r'\*{3}\s+START OF TH(E|IS) PROJECT GUTENBERG EBOOK' , line ):
        flag = True
        line = ''
    elif re.search( r'\*{3}\s+END' , line ):
        flag = False

    if flag == True:
        out.write(  line )
