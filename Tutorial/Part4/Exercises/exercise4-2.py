
### code to divide the novel into segments.
### The number of segments is determined by variable numberOfSegments

import re

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


data = dict()

count = 0
for s in segments:
    count += 1
    hits = re.findall( r'\bart(ist)?' , s , re.IGNORECASE )
    data[ count ] = len( hits )



import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

fig = plt.figure( figsize=( 12 , 4 ) )
ax = plt.axes()

ax.plot( data.keys() , data.values() , color = '#930d08' , linestyle = 'solid')

ax.set_xlabel('Section')
ax.set_ylabel('Frequency')

ax.set_title( 'A Portrait of the Artist')
plt.show()
