import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

ttRatio = [ 0.24 , 0.29 , 0.31 , 0.19 , 0.22 , 0.24 ]
sentLen = [ 18.5 , 21.7 , 32.6 , 26.9 , 21.3 , 36.8 ]

colors = ( '#a0061a' , '#a0061a' ,'#a0061a' , '#1607ed' , '#1607ed', '#1607ed'  )

fig = plt.figure()
ax = plt.axes()

ax.scatter( ttRatio , sentLen , alpha=0.8, c=colors, edgecolors='none', s=30, label=None )

ax.set_xlabel('Type-token ratio')
ax.set_ylabel('Average number of words per sentence')

legendDict = {"#a0061a":'Gothic novel' , "#1607ed":'History novel'}


plt.title('Matplot scatter plot')

for colour in legendDict:
    plt.scatter( [], [], c = colour , label = legendDict[colour] )


plt.legend(loc=3 , frameon=True )


ax.set_title( 'Analysis of Gothic of History novels' )

plt.savefig('scatterplot.png')
