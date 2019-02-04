first = 'vladimir'
last = 'nabokov'

fullName = last[0].upper() + last[1:len(last)]
fullName += ', '

## N.B.
### fullName += ', '
## is the same as
## fullName = fullName + ', ' 

fullName += first[0].upper() + first[1:len(first)]
fullName += '.'

print( fullName )


## A second and more simple solution:
fullName = last.title() + ', ' + first.title() + '.'
print( fullName )
