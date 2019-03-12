import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

freq = dict()

freq[100] = 45
freq[200] = 60
freq[300] = 70
freq[400] = 56
freq[500] = 49
freq[600] = 44
freq[700] = 42
freq[800] = 38

fig = plt.figure()
ax = plt.axes()

ax.plot( freq.keys() , freq.values() , color = '#930d08' , linestyle = 'dashdot')

ax.set_xlabel('Section')
ax.set_ylabel('Frequency')

ax.set_ylim( 0 , max( freq.values() ) + 10 )
ax.set_xlim( 0, 900 )

ax.set_title( 'A Room with a View')

plt.savefig('linechart.png')
