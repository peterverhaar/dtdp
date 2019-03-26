import re
import os
from os.path import join
import dtdpTdm as dtdp

out = open( 'data.csv' , 'w' )
dir = 'Corpus'

## make a heade
out.write( 'title,tokens,sentences,syllables\n' )


for file in os.listdir( dir ):
    if re.search( r'[.]txt' , file ):
        fileName = join( dir , file )
        print("Analysing " + fileName + " ...")
        out.write( fileName + ',' )
        print("Calculating number of tokens")
        out.write( str( dtdp.numberOfTokens( fileName ) ) )
        out.write( ',')
        print("Calculating number of sentences")
        out.write( str( dtdp.numberOfSentences( fileName ) ) )
        out.write( ',')
        print("Calculating number of syllables")
        out.write( str( dtdp.numberOfSyllables( fileName ) ) )
        out.write( '\n')

out.close()
