quote = "We cast a shadow on something wherever we stand, and it is no good moving from place to place to save things; because the shadow always follows. Choose a place where you won’t do harm - yes, choose a place where you won’t do very much harm, and stand in it for all you are worth, facing the sunshine."

words = quote.split(' ')
print( 'The quote contains {} words.'.format( len(words) ) )

count = 0

for w in words:
    if w.lower() == 'place':
        count+= 1

print( "There are {} occurrences of the word 'place'.".format( count ) )
