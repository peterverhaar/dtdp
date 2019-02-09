
sonnet = open( 'prufrock.txt' )
out = open( 'data2.txt' , 'w' )

totalNrCharacters = 0
lineNr = 0
max = ''


for line in sonnet:
    if len(line.strip()) > 0:
        totalNrCharacters += len(line)
        lineNr += 1
        if len(line) > len(max):
            max = line.strip()

out.write( 'Total number of characters: {}\n'.format( totalNrCharacters ) )
out.write( 'Number of lines: {}\n'.format( lineNr ) )
out.write( 'Average number of characters per line: {}\n'.format( totalNrCharacters / lineNr ) )
out.write( "Longest line: '{}'\n".format( max ) )
