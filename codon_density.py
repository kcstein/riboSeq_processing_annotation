# inFile = .density ; outFile = .codon

import sys

countsDict = {}
codonDict = {}

inFile = open(sys.argv[1], 'r')
line = inFile.readline()
while line != '':
    fields = line.split()
    name = fields[0]
    position = int(fields[1])
    codon = str(fields[2])
    density = float(fields[3])

    line = inFile.readline()    
    fields = line.split()
    codon = str(codon + str(fields[2]))
    density = density + float(fields[3])

    line = inFile.readline()
    fields = line.split()
    codon = str(codon + str(fields[2]))
    density = density + float(fields[3])

    if name not in countsDict:
        countsDict[name] = {}
        codonDict[name] = {}

    countsDict[name][position] = density
    codonDict[name][position] = codon	
    line=inFile.readline()

print 'OK!'

outFile=open(sys.argv[2], 'w')
for G in sorted(countsDict.keys()) and sorted(codonDict.keys()):
    for x in sorted(countsDict[G].keys()) and sorted(codonDict[G].keys()):
        outFile.write(str(G) + '\t' + str((x-1)/3+2) + '\t' + str(codonDict[G][x])  + '\t' + str(countsDict[G][x]) + '\n')
    