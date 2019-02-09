
## For this code to work, a text files named “Prufrock.txt”
## needs to be in the same folder as the Python code.
text = open( "Prufrock.txt" , encoding = 'utf-8' )
for line in text:
    print(line)
