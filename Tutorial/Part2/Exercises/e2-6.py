
sonnet = open( 'sonnet116.txt' )

lineNr = 0


for line in sonnet:
    lineNr += 1
    print('{}.\t{}'.format( lineNr , line ) )
