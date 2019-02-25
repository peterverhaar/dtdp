
import string
import re

import matplotlib.pyplot as plt

### code to divide the novel into segments.
### The number of segments is determined by variable numberOfSegments


## function to tokenise a string into words
def tokenise( text ):
    tokens = []
    text = text.lower()
    text = re.sub( '--' , ' -- ' , text)
    words = re.split( r'\s+' , text )
    for w in words:
        w = w.strip( string.punctuation )
        if re.search( r"[a-zA-Z']" , w ):
            tokens.append(w)
    return tokens




numberOfSegments = 30
segments = []

novel = open('APortraitOfTheArtist.txt')

## The read() function can read in the entire file as a single string
fullText = novel.read()
allWords = re.split( r'\s+' , fullText )

segmentSize = int( len(allWords) / numberOfSegments )

countWords = 0
text = ''

for word in allWords:
    countWords += 1
    text += word + ' '

    ## This line below used the modulo operator:
    ## We can use it to test if the first number is
    ## divisible by the second number
    if countWords % segmentSize == 0:
        segments.append(text.strip())
        text = ''

x = dict()
y = dict()

count = 0
for s in segments:
    count += 1
    hits = re.findall( r'\bmother' , s , re.IGNORECASE )
    x[ count ] = len( hits )
    hits = re.findall( r'\bfather' , s , re.IGNORECASE )
    y[ count ] = len( hits )



plt.style.use('seaborn-whitegrid')

fig = plt.figure( )
ax = plt.axes()
ax.scatter( x.values() , y.values()  , alpha=0.8, edgecolors='none', s=30, label=None )
ax.set_xlabel('Father')
ax.set_ylabel('Mother')

ax.set_title( 'A Portrait of the Artist')

for label in x.keys():
    ax.annotate( label , (x[label] , y[label] + 0.4))

plt.show()
