import re
import string

textFile = 'APortraitOfTheArtist.txt'
maxNrWords = 75

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

novel = open( textFile )

## Calculate the frequencies of all the words
freq = dict()

for paragraph in novel:
    words = tokenise(paragraph)
    for w in words:
        freq[w] = freq.get(w,0)+1


## determine the 50 most frequent words, and
## place these in a dictionary named mostFreq()

sortedWords = reversed( sorted( freq , key=lambda x: freq[x]) )
mostFreq = dict()

count = 0
for w in sortedWords:
    mostFreq[w] = freq[w]
    count += 1
    if count == maxNrWords:
        break


import matplotlib.pyplot as plt

fig = plt.figure( figsize=( 12 , 5 ) )
ax = plt.axes()

ax.bar( mostFreq.keys() , mostFreq.values() , width = 0.9 , alpha = 0.5 , color = '#03017a')

ax.set_xlabel('Words')
ax.set_ylabel('Frequencies')
ax.set_title( 'A Portrait of the Artist as a Young Man')

## labels for the ticks on the X-axis need to
## be shown vertically to improve the readability
plt.xticks(rotation=90)

plt.show()
