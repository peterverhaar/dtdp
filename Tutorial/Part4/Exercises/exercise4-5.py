formats = {
'quarto':3524 ,
'16mo':246 ,
'folio':877 ,
'octavo':1475
}



import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

fig = plt.figure( figsize=( 4 , 4 ) )
ax = plt.axes()


ax.bar( formats.keys() , formats.values() , width = 0.9 , alpha = 0.7 , color = '#03017a')

ax.set_xlabel('Format')
ax.set_ylabel('Number of titles')

ax.set_title( 'STCN data')
plt.show()
