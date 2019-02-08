plays = [ 'Comedy of Errors' ,
'Henry VI, Part I' ,
'Henry VI, Part II' ,
'Henry VI, Part III' ,
'Richard III' ,
'Taming of the Shrew' ,
'Titus Andronicus' ,
'Romeo and Juliet' ,
'Two Gentlemen of Verona' ,
'Love\'s Labour\'s Lost' ,
'Richard II' ,
'Midsummer Night\'s Dream' ]

plays.append('Macbeth')
plays.append('Othello')
plays.append('Romeo and Juliet')
plays.append('Timon of Athens')
plays.append('Titus Andronicus')

print( 'This list contains {} plays.'.format( len(plays) ) )
print( "The first play in the list is '{}'.".format( plays[0] ) )
print( "The last play in the list is '{}'.".format( plays[-1] ) )

for p in sorted(plays):
    print(p)
