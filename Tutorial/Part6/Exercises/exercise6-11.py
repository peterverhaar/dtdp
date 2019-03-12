import os
from os.path import join
import dtdpTdm as tdm
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

dir = 'Corpus'

titles = []
positive = []
negative = []

for file in os.listdir( dir ):
    if re.search( r'[.]txt' , file ):

        title = re.sub( r'\.txt' , '' , file )
        titles.append( title )
        print(title)

        fullPath = join( dir , file )
        tokens = tdm.numberOfTokens( fullPath )
        count = tdm.countOccurrencesLexicon( fullPath , 'positive.txt' )
        positive.append(count/tokens)
        count = tdm.countOccurrencesLexicon( fullPath , 'negative.txt' )
        negative.append(count/tokens)




import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')



fig = plt.figure( figsize=( 12 , 12 )  )
ax = plt.axes()

ax.scatter( positive , negative , alpha=0.8,  edgecolors='none', s=30, label=None )


for i in range( 0 , len( titles ) ):
    ax.annotate( titles[i] , ( positive[i] , negative[i]  )  )


ax.set_xlabel('Positive')
ax.set_ylabel('Negative')


ax.set_title( 'Sentiment analysis' )

plt.show()
