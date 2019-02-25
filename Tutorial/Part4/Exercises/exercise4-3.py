
import string
import re

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

ttr = dict()

count = 0
for s in segments:
    count += 1
    tokens = tokenise(s)
    ### set() leaves only the unique elements in a list
    types = set(tokens)
    ttr[ count ] = len(types) / len( tokens )



import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

fig = plt.figure( figsize=( 12 , 4 ) )
ax = plt.axes()

ax.bar( ttr.keys() , ttr.values() , width = 0.7 , alpha = 0.8 , color = '#03017a')

ax.set_xlabel('Section')
ax.set_ylabel('Frequency')

ax.set_title( 'A Portrait of the Artist')
plt.show()
