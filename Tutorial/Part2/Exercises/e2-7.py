
freq = dict()
text = open("ARoomWithAView.txt" , encoding = 'utf-8' )
out = opn( "mostFrequentWords.txt" , 'w' )

for line in text:
    line = line.lower()
    words = line.split(' ')
    for w in words:
        w = w.strip()
        freq[w] = freq.get( w ,0 ) + 1

sorted = reversed( sorted( freq , key=lambda x: freq[x]) )

count = 0
for w in sorted:
    out.write( str(count) + ': ' +  w + ' => ' + str( freq[w] ) + '\n' )
    if count == 50:
        break
    count += 1
