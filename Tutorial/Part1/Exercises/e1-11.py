first = 'vladimir'
last = 'nabokov'

fullName = last[0].upper() + last[1:len(last)]
fullName += ', '

## N.B. fullName += is the same as
## fullName = fullName + 

fullName += first[0].upper()
fullName += '.'

print( fullName )
