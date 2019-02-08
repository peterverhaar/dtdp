

data = dict()

data["firstName"] = 'Louis'
data["lastName"] = 'Elsevier'
data["profession"] = 'printer'
data["yob"] = 1540
data["yod"] = 1617
data["pob"] = 'Leuven'
data["pod"] = 'Leiden'

sentence = '{} {} was a {}. '.format( data['firstName'] , data['lastName'] , data['profession']  )
sentence += 'He was born in {} in {} and died in {} in {}.'.format( data["yob"] , data["pob"] , data["yod"] ,data["pod"]  )

print( sentence )
