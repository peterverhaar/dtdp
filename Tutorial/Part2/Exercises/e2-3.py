isbn = {
9780143105985 : 'White Noise' ,
9780241984536 : 'Libra' ,
9781925480665 : 'Mao II' ,
9781447289395 : 'Underworld' ,
9780743595728 : 'The Body Artist' ,
9781925480665 : 'Cosmopolis' ,
9780330524919 : 'Falling man' ,
9781439169971 : 'Point Omega'
}

isbn[9781501138072] = 'Zero K'

index = 9781447289395
print( "\nThe ISBN of the novel '{}' is {}.\n".format( isbn[index] , index ) )

for novel in isbn:
    print( isbn[novel] + ' (' + str(novel) + ')' )
