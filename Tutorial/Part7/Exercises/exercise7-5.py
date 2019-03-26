
import pandas as pd

df = pd.read_csv( 'data.csv' )


import seaborn as sns
import matplotlib.pylab as plt


ax = sns.heatmap( df.corr() , linewidth=0.5 , cmap="YlGnBu" )
plt.show()
