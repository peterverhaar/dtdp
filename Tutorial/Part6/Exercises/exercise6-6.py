import os
from os.path import join

import dtdpTdm as tdm
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

dir = 'Corpus'

titles = []
sentenceLength = []


for file in os.listdir( dir ):
    if re.search( r'[.]txt' , file ):

        fullPath = join( dir , file )
        print( 'Analysing ' +  fullPath + '...' )
        tokens = tdm.numberOfTokens( fullPath )
        sentences = tdm.numberOfSentences( fullPath )

        sentenceLength.append( tokens / sentences  )


        title = re.sub( r'\.txt' , '' , file )
        titles.append( title )


import matplotlib.pyplot as plt

fig = plt.figure( figsize=( 12 , 5 ) )
ax = plt.axes()

ax.bar( titles , sentenceLength , width = 0.6 , alpha = 0.5 , color = '#03017a')

ax.set_xlabel('Texts')
ax.set_ylabel('Words')
ax.set_title( 'Average number of words per sentences')

## labels for the ticks on the X-axis need to
## be shown vertically to improve the readability
plt.xticks(rotation=90)

plt.show()
