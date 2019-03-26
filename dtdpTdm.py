
import string
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import xml.etree.ElementTree as ET
import requests
import zipfile
import math
import os
from os.path import isfile, join , isdir
import string

lines = list()
taggedLines = list()
currentFile = ''

freqText = dict()

sentiments = dict()

def initalise():
    lines.clear()
    taggedLines.clear()


def readFile( file ):

    global lines
    global currentFile

    currentFile = file

    initalise()

    if re.search( r'\.txt$' , file ):
        try:
            text = open( file , encoding = 'utf-8' )

            for line in text:
                lines.append(line)
        except:
            print( "Cannot read " + file + " !" )



def concordance( file , searchTerm , window ):

    global lines
    global currentFile

    if file != currentFile:
        readFile(file)

    concordance = []
    regex = searchTerm

    for line in lines:
        line = line.strip()

        if re.search( regex , line , re.IGNORECASE ):

            extract = ''

            position = re.search( regex , line , re.IGNORECASE ).start()
            start = position - len( searchTerm ) - window ;
            fragmentLength = start + 2 * window  + len( searchTerm )
            if fragmentLength > len( line ):
                fragmentLength = len( line )

            if start < 0:

                whiteSpace = ''
                i = 0
                while i < abs(start):
                    whiteSpace += ' '
                    i += 1
                extract = whiteSpace + line[ 0 : fragmentLength ]
            else:
                extract = line[ start : fragmentLength ]

            if re.search( '\w' , extract ) and re.search( regex , extract ):
                concordance.append( extract )
    return concordance



def divideIntoSegments( file , numberOfSegments ):

    segments = []

    textFile = open( file )

    ## The read() function can read in the entire file as a single string
    fullText = textFile.read()
    allWords = re.split( r'\s+' , fullText )

    segmentSize = int( len(allWords) / numberOfSegments )

    countWords = 0
    text = ''

    for word in allWords:
        countWords += 1
        text += word + ' '

        ## This line below used the modulo operator:
        ## We can use it to test if the first number is
        ## divisible by the second number
        if countWords % segmentSize == 0:
            segments.append(text.strip())
            text = ''
    return segments


def collocation( file , regex , distance ):

    global lines
    global currentFile

    if file != currentFile:
        readFile(file)


    freq = dict()

    paragraph = ''

    parLength = 0

    for line in lines:
        line = line.strip()
        if parLength < 100:
            parLength += len(line)
            paragraph += line + ' '
        else:
            parLength = 0
            words = tokenise( paragraph )
            i = 0
            for w in words:
                if re.search( regex , w , re.IGNORECASE ):

                    match = re.search( regex , w , re.IGNORECASE )
                    searchTerm = match.group(0)

                    for x in range( i - distance , i + distance ):
                        if x >= 0 and x < len(words) and searchTerm != words[x]:
                            if len(words[x]) > 0:
                                freq[ words[x] ] = freq.get( words[x] , 0 ) + 1

                i += 1
            paragraph = ''


    sortedWords = reversed( sorted( freq , key=lambda x: freq[x]) )
    sortedFreq = dict()

    for w in sortedWords:
        sortedFreq[w] = freq[w]

    return sortedFreq


def numberOfSentences(file):
    fullText = open( file , encoding = 'utf-8' )
    s = sent_tokenize(fullText.read())
    return len(s)




# function to tokenise a string into words
def tokenise( text ):
    tokens = []
    text = text.lower()
    text = re.sub( '--' , ' -- ' , text)
    words = re.split( r'\s+' , text )
    for w in words:
        w = w.strip( string.punctuation )
        if re.search( r"[a-zA-Z']" , w ):
            tokens.append(w)
    return tokens


def numberOfSyllables(file):

    global lines
    global currentFile

    if file != currentFile:
        readFile(file)

    nrSyllables = 0
    freq = calculateWordFrequencies( file )
    for w in freq:
        nrSyllables += countSyllables(w) * freq[w]
    return ( nrSyllables )

def countSyllables( word ):
    pattern = "e?[aiouy]+e*|e(?!d$|ly).|[td]ed|le\$|ble$|a$"
    syllables = re.findall( pattern , word )
    return len(syllables)

def fleschKincaid( file ):

    global lines
    global currentFile

    if file != currentFile:
        readFile(file)


    totalWords = numberOfTokens(file)
    totalSentences = numberOfSentences(file)
    totalSyllables = numberOfSyllables(file)

    fk = 0.39 * (  totalWords / totalSentences )
    fk = fk + 11.8 * ( totalSyllables / totalWords )
    fk = fk - 15.59
    return fk


def calculateWordFrequencies( file ):

    global lines
    global currentFile

    if file != currentFile:
        readFile(file)

    freq = dict()

    for line in lines:
        words = tokenise( line )
        for w in words:
            freq[w] = freq.get( w , 0 ) + 1

    return freq

def mostFrequentWords( file , maxNrWords ):

    freq = calculateWordFrequencies( file )
    freq = removeStopWords( freq )

    sortedWords = reversed( sorted( freq , key=lambda x: freq[x]) )
    mostFreq = dict()

    count = 0
    for w in sortedWords:
        mostFreq[w] = freq[w]
        count += 1
        if count == maxNrWords:
            break

    return mostFreq


def removeStopWords( freq ):

    filtered = dict()
    stopWords = set(stopwords.words('english'))

    for w in freq:
            if w not in stopWords:
                filtered[w] = freq[w]

    return filtered


def countOccurrences( regex , file ):

    global lines
    global currentFile
    count = 0

    if file != currentFile:
        readFile(file)

    for l in lines:
        if re.search( regex , l , re.IGNORECASE ):
            count += 1
    return count


def numberOfTypes( file ):

    global lines
    global currentFile

    if file != currentFile:
        readFile(file)

    nrTypes = 0
    freq = calculateWordFrequencies( file )
    nrTypes =  len(freq)
    return ( nrTypes )

def typeTokenRatioCurve( file , step ):

    text = open( file )
    fullText = text.read()
    allWords = tokenise( fullText )

    ttr = dict()

    count = 0
    freq = dict()

    for w in allWords:
        count += 1
        freq[w] = freq.get( w ,0 ) + 1
        if count % step == 0:
            ttr[ count ] = len(freq)
    return ttr

def numberOfTokens(  file ):

    global lines
    global currentFile

    if file != currentFile:
        readFile(file)

    nrTokens = 0
    freq = calculateWordFrequencies(  file )
    for w in freq:
        nrTokens += freq[w]
    return ( nrTokens )

def tdIdf( corpus , file ):

    global freqText
    file = os.path.basename( file )

    freq = dict()


    txt = []

    ## Formula is as follows: tf-idf= log⁡(⁡ N /df ),
    # tf being the number of times a term appears in a document,
    # N being the total number of documents
    # df being the number of documents in which the term appears.

    if len( freqText ) == 0:

        fnames = os.listdir( corpus )
        for i in fnames:
            if re.search( '[.]txt$' , i):
                txt.append( i )

        ## N is total number of texts
        N = len(txt)

        for t in txt:
            textWords = []
            text = open( join( corpus , t ) , encoding = 'utf-8' )

            for line in text:
                words = tokenise( line )
                for w in words:
                    freq[w] = freq.get( w , 0 ) + 1
                    freqText[ (t , w ) ] = freq.get( (t , w ) , 0 ) + 1


        idf = dict()
        ## df is number of texts in which the term appears

        for word in freq:
            df = 0

            for text in txt:
                if ( text , word ) in freqText:
                    df += 1

            idfW = math.log( N / df )
            idf[ word ] = idfW

            for text in txt:
                if ( text , word ) in freqText:
                    freqText[ ( text , word ) ] = 1 + freqText[ ( text , word ) ] * idf[ word ]

        print( 'Done: Calculations made.' )


    freqIdf = dict()
    allWords = dict()

    for w in freqText:
        print(freqText[w][1])
        allWords.append( freqText[w][1] )

    for w in allWords:
        if( file , w ) in freqText:
            freqIdf[w] = freqText[ ( file , w ) ]
            i += 1
            if i == max:
                break

    return freqIdf


def posTagger( file ):

    global lines
    global taggedLines

    global currentFile
    if file != currentFile:
        readFile(file)

    print("Adding POS tags for {} ...".format(file)  )

    for line in lines:
        taggedLine = ''
        words = word_tokenize(line)
        pos = nltk.pos_tag(words)

        for p in pos:
            taggedLine += p[1] + ' '
        taggedLines.append( taggedLine )


def countPosTag( file , posRe ):
    global taggedLines
    global lines

    countTag = 0

    global currentFile
    if file != currentFile:
        readFile(file)
        taggedLines.clear()

    if len(taggedLines) == 0:
        posTagger( file )

    for line in taggedLines:
        hits = re.findall( posRe , line )
        #print(line)
        #for h in hits:
            #print(h)
        countTag += len(hits)

    return countTag

def countOccurrencesLexicon( file , lexiconFile ):

    global lines

    global currentFile
    if file != currentFile:
        readFile(file)

    countOccurrences = 0
    lexicon = open( lexiconFile , encoding = 'utf-8')
    listOfWords = []

    for line in lexicon:
        line = line.strip()
        listOfWords.append(line.lower() )

    freq = calculateWordFrequencies( file )
    for w in freq:
        if w in listOfWords:
            countOccurrences += freq[w]

    return countOccurrences

freqText = dict()

def tdIdf( corpus , focusText ):

    ## freqText is a dictionary with frequencies of all Words in the corpus
    global freqText

    freq = dict()

    #list to kep track of all the texts in the corpus
    txt = []

    ## Formula is as follows: tf-idf= tf * log⁡(⁡ N /df ),
    # tf being the number of times a term appears in a document,
    # N being the total number of documents
    # df being the number of documents in which the term appears.

    if len( freqText ) == 0:

        fnames = os.listdir( corpus )
        for i in fnames:
            if re.search( '[.]txt$' , i):
                txt.append( i )

        ## N is total number of texts
        N = len(txt)

        if focusText not in txt:
            print("The file you mentioned is not in the corpus!")

        for t in txt:
            textWords = []
            text = open( join( corpus , t ) , encoding = 'utf-8' )

            for line in text:
                words = tokenise( line )
                for w in words:
                    freq[w] = freq.get( w , 0 ) + 1
                    freqText[ (t , w ) ] = freq.get( (t , w ) , 0 ) + 1


        idf = dict()
        ## df is number of texts in which the term appears

        for word in freq:
            df = 0

            for text in txt:
                if ( text , word ) in freqText:
                    df += 1

            idfW = math.log( N / df )
            idf[ word ] = idfW

            for text in txt:
                if ( text , word ) in freqText:
                    freqText[ ( text , word ) ] = freqText[ ( text , word ) ] * idf[ word ]

        print( 'Done: Calculations made.' )


    freqIdf = dict()
    allWords = []


    for w in freqText:
        allWords.append(w[1])

    for w in allWords:

        if ( focusText , w ) in freqText:
            if freqText[ ( focusText , w ) ] > 0 and not( re.search( '[-]' , w ) ):
                freqIdf[w] = freqText[ ( focusText , w ) ]


    return freqIdf
