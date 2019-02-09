week = [ "Monday" , "Tuesday" , "Wednesday" , "Thursday" ,"Friday" ]

print( week[3] )
# This prints "Thursday"

print( week[-1] )
# This prints "Friday"

print( len(week) )
# This prints 5

week.append("Saturday")
week.append("Sunday")

print( "The list now contains {} items.".format( len(week)))
# This prints the following sentence:
# 'The list now contains 7 items.'
