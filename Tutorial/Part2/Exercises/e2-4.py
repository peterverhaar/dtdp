eu = {
'Italy':'Rome' , 'Luxembourg':'Luxembourg' , 'Belgium':'Brussels' , 'Denmark':'Copenhagen' , 'Finland':'Helsinki' , 'France':'Paris' , 'Slovakia':'Bratislava' , 'Slovenia':'Ljubljana' , 'Germany':'Berlin' , 'Greece':'Athens' , 'Ireland':'Dublin' , 'Netherlands':'Amsterdam' , 'Portugal':'Lisbon' , 'Spain':'Madrid' , 'Sweden':'Stockholm' , 'United Kingdom':'London' , 'Cyprus':'Nicosia' , 'Lithuania':'Vilnius' , 'Czech Republic':'Prague' , 'Estonia':'Tallin' , 'Hungary':'Budapest' , 'Latvia':'Riga' , 'Malta':'Valetta' , 'Austria':'Vienna' , 'Poland':'Warsaw' , 'Croatia':'Zagreb' ,'Romania':'Bucharest' , 'Bulgaria':'Sofia' }

print( 'The EU currently has {} member countries:'.format( len(eu) ) )

for country in sorted(eu):
    print( country )

print('\n')

sorted = sorted( eu , key=lambda x: eu[x])


for country in sorted:
    print( 'The capital of {} is {}.'.format( country , eu[country] ) )
