

freq = dict()
text = open("Prufrock.txt" , encoding = 'utf-8' )
for line in text:
    line = line.lower()
    words = line.split(' ')
    for w in words:
        w = w.strip()
        freq[w] = freq.get( w ,0 ) + 1

sorted = reversed( sorted( freq , key=lambda x: freq[x]) )
for w in sorted:
    print( w + ' => ' + str( freq[w] ) )
