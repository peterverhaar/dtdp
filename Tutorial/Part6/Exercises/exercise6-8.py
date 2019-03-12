import os
from os.path import join
import dtdpTdm as tdm
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

dir = 'Corpus'

titles = []
sentLength = []
wordLength = []

for file in os.listdir( dir ):
    if re.search( r'[.]txt' , file ):

        title = re.sub( r'\.txt' , '' , file )
        titles.append( title )
        print(title)

        fullPath = join( dir , file )

        tokens = tdm.numberOfTokens( fullPath )
        syllables = tdm.numberOfSyllables( fullPath )

        tokens = tdm.numberOfTokens( fullPath )
        sentences = tdm.numberOfSentences( fullPath )

        sentLength.append(  tokens / sentences )
        wordLength.append( syllables / tokens )

%matplotlib inline
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')



fig = plt.figure( figsize=( 12 , 5 )  )
ax = plt.axes()

ax.scatter( sentLength , wordLength , alpha=0.8,  edgecolors='none', s=30, label=None )


for i in range( 0 , len( titles ) ):
    ax.annotate( titles[i] , ( sentLength[i] -1.5 , wordLength[i] + 0.005 )  )


ax.set_xlabel('Average number of words per sentence')
ax.set_ylabel('Average number of syllables per word')



plt.title('Matplot scatter plot')


ax.set_title( 'Word length and Sentence length' )

plt.show()
