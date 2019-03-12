import os
from os.path import join

import dtdpTdm as tdm
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

dir = 'Corpus'

titles = []
fk = []


for file in os.listdir( dir ):
    if re.search( r'[.]txt' , file ):

        fullPath = join( dir , file )
        print( 'Analysing ' +  fullPath + '...' )
        tokens = tdm.numberOfTokens( fullPath )

        title = re.sub( r'\.txt' , '' , file )
        titles.append( title )

        score = tdm.fleschKincaid( fullPath )
        fk.append(score)


%matplotlib inline
import matplotlib.pyplot as plt

fig = plt.figure( figsize=( 12 , 5 ) )
ax = plt.axes()

ax.bar( titles , fk , width = 0.6 , alpha = 0.5 , color = '#03017a')

ax.set_xlabel('Texts')
ax.set_ylabel('Complexity')
ax.set_title( 'Research project')

## labels for the ticks on the X-axis need to
## be shown vertically to improve the readability
plt.xticks(rotation=90)

plt.show()
