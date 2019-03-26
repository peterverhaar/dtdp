
import dtdpTdm as dtdp

dir = 'Corpus'
text = 'VanityFair.txt'

freq = dtdp.tdIdf( dir , text )

'''
sortedList = reversed(sorted( freq , key=lambda x: freq[x]))

for w in sortedList:
    print( w + ' => ' + str( freq[w] ) )
'''


%matplotlib inline

import matplotlib.pyplot as plt
from wordcloud import WordCloud

wordcloud = WordCloud( background_color="white",  width=1500,height=1000, max_words= 100,relative_scaling=1,normalize_plurals=False).generate_from_frequencies(freq)


plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
