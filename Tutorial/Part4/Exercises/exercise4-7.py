
import matplotlib.pyplot as plt


title = [
 'The Wolf of Wall Street' ,
 'Prisoners' ,
 '12 Years a Slave' ,
 'Furious 6' ,
 'Guardians of the Galaxy' ,
 'Interstellar' ,
 'John Wick' ,
 'Kingsman: The Secret Service' ,
 'Bahubali: The Beginning' ,
 'Star Wars: Episode VII - The Force Awakens' ,
 'Fifty Shades of Grey' ,
 'Mad Max: Fury Road' ,
 'Split' ,
 'Sing' ,
 'The Great Wall' ,
 'La La Land'
]

year = [
 2013 ,
 2013 ,
 2013 ,
 2013 ,
 2014 ,
 2014 ,
 2014 ,
 2014 ,
 2015 ,
 2015 ,
 2015 ,
 2015 ,
 2016 ,
 2016 ,
 2016 ,
 2016
]

genre = [
 'Biography' ,
 'Crime' ,
 'Biography' ,
 'Action' ,
 'Action' ,
 'Adventure' ,
 'Action' ,
 'Action' ,
 'Action' ,
 'Action' ,
 'Drama' ,
 'Action' ,
 'Horror' ,
 'Animation' ,
 'Action' ,
 'Comedy'
]

rating = [
 8.2 ,
 8.1 ,
 8.1 ,
 7.1 ,
 8.1 ,
 8.6 ,
 7.2 ,
 7.7 ,
 8.3 ,
 8.1 ,
 4.1 ,
 8.1 ,
 7.3 ,
 7.2 ,
 6.1 ,
 8.3
]

revenue = [
 116.87 ,
 60.96 ,
 56.67 ,
 238.67 ,
 333.13 ,
 187.99 ,
 43.0 ,
 128.25 ,
 6.5 ,
 936.63 ,
 166.15 ,
 153.63 ,
 138.12 ,
 270.32 ,
 45.13 ,
 151.06
]

colour = []


legendDict = { 2013 :'#a0061a' , 2014 :'#1607ed' , 2015 :'#5607aa' , 2016 :'#aa07ed' ,}

for y in year:
    colour.append( legendDict[y] )



plt.style.use('seaborn-whitegrid')

fig = plt.figure( figsize=( 12 , 7 ) )
ax = plt.axes()
ax.scatter( rating , revenue  , alpha=0.8, s=30, label=None , c = colour )
ax.set_xlabel('Rating')
ax.set_ylabel('Revenue')
ax.set_ylim( -200 , 1200 )

ax.set_title( 'IMDB data')

for i in range( 0 , len( title ) ):
    ax.annotate( title[i] , ( rating[i] - 0.2 , revenue[i] + 30 ))

for year in legendDict:
    plt.scatter( [], [], c = legendDict[year] , label = year)
plt.legend(loc=2 , frameon=True )

plt.show()
