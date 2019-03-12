import matplotlib.pyplot as plt

freq = dict()

freq['the'] = 2254
freq['of'] = 1365
freq['a'] = 1123
freq['i'] = 1094
freq['and'] = 930
freq['to'] = 870
freq['was'] = 668
freq['in'] = 602

fig = plt.figure()
ax = plt.axes()

bar_width = 0.45
opacity = 0.8

ax.bar( freq.keys() , freq.values() , width = bar_width , alpha = opacity , color = '#03017a')
ax.set_xlabel('Words')
ax.set_ylabel('Frequencies')
ax.set_title( 'A Room with a View')

plt.show()
