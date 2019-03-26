import pandas as pd

df = pd.read_csv( 'data.csv' )

for index , column in df.iterrows():
    print( '{} contains {} tokens.'.format( column["title"] , column["tokens"] ) )
