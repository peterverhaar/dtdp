
# # Exercise 3.5
#
# The file "stcn.txt" (https://raw.githubusercontent.com/peterverhaar/dtdp/master/Texts/stcn.txt) is a small export from the Short Title Catalogue of the Netherlands. It offers information on 50 titles printed by members of the Elzevier family. Try to convert the export as it is given in the original file to a CSV file. A CSV is file format in which all the values are separated by a comma. The new CSV file should contain the following values: BOOK_ID, full name of the author, year, format and the full title. The full name of the author must be given as follows: ‘First name + SPACE + Last name’.
# The CSV file must start with a header which specifies names for all the columns. The output file should be named ‘data.csv’.
#



import re

stcn = open( 'stcn.txt' )
out = open( 'data.csv' , 'w' )

data = dict()

## print the header
out.write( 'BOOK_ID,fullName,year,format,title\n' )

for line in stcn:
    print(line)
    if re.search( r'^RECORD' , line ) and len(data) > 0:

        ## remove commas
        for value in data:
            data[value] = re.sub( ',' , '' , data[value] )

        ## Create variable fullName, using the first and the last name
        fullName = data.get('first' , '')
        if re.search( '\w' , fullName ):
            fullName += ' '
        fullName += data.get('last' , '')

        ## write the data to a CSV file
        out.write('{},{},{},{},{}\n'.format( data.get('book_id' , '') , fullName , data.get('year' , '') , data.get('format' , '') , data.get('title' , '') )  )

        ## remove all values from the data dictionary
        data.clear()

    elif re.search( r'^YEAR' , line ):
        line = re.sub( 'YEAR: ' , '' , line )
        data['year'] = line.strip()
    elif re.search( r'^FORMAT' , line ):
        line = re.sub( 'FORMAT: ' , '' , line )
        data['format'] = line.strip()
    elif re.search( r'^TITLE' , line ):
        line = re.sub( 'TITLE: ' , '' , line )
        data['title'] = line.strip()
    elif re.search( r'^B_ID' , line ):
        line = re.sub( 'B_ID: ' , '' , line )
        data['book_id'] = line.strip()
    elif re.search( r'^B_ID' , line ):
        line = re.sub( 'B_ID: ' , '' , line )
        data['book_id'] = line.strip()
    elif re.search( r'^NAME_LAST' , line ):
        line = re.sub( 'NAME_LAST: ' , '' , line )
        data['last'] = line.strip()
    elif re.search( r'^NAME_FIRST' , line ):
        line = re.sub( 'NAME_FIRST: ' , '' , line )
        data['first'] = line.strip()

## print the vary last record

if len(data) > 0:

    ## remove commas
    for value in data:
        data[value] = re.sub( ',' , '' , data[value] )

    fullName = data.get('first' , '')
    if re.search( '\w' , fullName ):
        fullName += ' '
    fullName += data.get('last' , '')

    out.write('{},{},{},{},{}\n'.format( data.get('book_id' , '') , fullName , data.get('year' , '') , data.get('format' , '') , data.get('title' , '') )  )

out.close()
