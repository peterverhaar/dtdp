import os
from os.path import join
import dtdpTdm as tdm
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

dir = 'Corpus'

colours = [ '#e8e551' , '#403cc1' , '#35872d' , '#cc37c7' , '#e89912' , '#8c1fb7' , '#4cdbbe' , '#6f6b72' , '#bfa2d6' , '#f9b298' , '#efef07' , '#63e24f' , '#f311f7' ]

files = []
titles = []

for file in os.listdir( dir ):
    if re.search( r'[.]txt' , file ):
        files.append( join( dir , file ) )
        title = re.sub( r'\.txt' , '' , file )
        titles.append( title )



%matplotlib inline
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

fig = plt.figure( figsize=( 12 , 12 ) )
ax = plt.axes()

for i in range( 0 , len(files) ):
    ttr = tdm.typeTokenRatioCurve( files[i] , 50 )
    ax.plot( ttr.keys() , ttr.values() , label = titles[i] , color = colours[i] , linestyle = 'solid')

ax.set_xlabel('Type')
ax.set_ylabel('Token')

ax.set_title( 'TTR Curves')

plt.legend(loc=2 , frameon=True )

plt.show()
        
