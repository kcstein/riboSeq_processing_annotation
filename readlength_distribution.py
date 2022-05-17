import sys

def rawdata(inputFile, outputFile):
            
    readDict = {}
    inFile = open(inputFile, 'r')
    line = inFile.readline()
    while line != '':
        fields = line.split()
        readseq = str(fields[5])        	#footprint seq
        readlength = str(len(readseq))       	#footprint length assigned as categorical string
        length = int(readlength)		#footprint length to add to length categories
    
        if readlength not in readDict:
            readDict[readlength]={}          
        
        if length in readDict[readlength]:
            readDict[readlength][length] = readDict[readlength][length] + 1
            
        else:
            readDict[readlength][length] = 1          
                
        line = inFile.readline()
    
    outFile = open(outputFile, 'w')
    for L in sorted(readDict.keys()):
        for x in sorted(readDict[L].keys()):
            outFile.write(str(L) + '\t' + str(readDict[L][x]) + '\n') 

if __name__=='__main__':
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    rawdata(inputFile, outputFile)