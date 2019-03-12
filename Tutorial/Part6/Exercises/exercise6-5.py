import os
from os.path import join


dir = 'Corpus'

for file in os.listdir( dir ):
    if re.search( r'[.]txt' , file ):
        print( join( dir , file ) )
