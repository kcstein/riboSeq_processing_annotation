"""

This script was initially written by Eugene Oh and Annemarie Becker as Supplementary Note 2. It has been modified by Justin Chartron and Kevin Stein

From a Bowtie alignment file, this script generates a file containing read density at each nucleotide in a reference file.

inputFile:
.map file generated by Bowtie default output.

outputFileP:
read density file for plus strand
    col0: genomic feature of interest
    col1: position along genome
    col2: read density at that position

refFile:
FASTA format of coding sequences, with entire sequences on single lines.

The length of each open reading frame is obtained directly from the fasta file used to generate the bowtie library.
Regions that are not observed within each gene are given a zero value.

"""

def rawdata(inputFile, refFile, outputFile):

    countsDict = {}
    refDict = {}
    ref=open(refFile,"r")
    line=ref.readline()
    while line != "":
        refgeneb = str(line[1:len(line)])
        refgene = refgeneb.strip()
        line=ref.readline()
        refseq = line.strip()
        refDict[refgene] = {i:c for i,c in enumerate(refseq, 1)}
        countsDict[refgene] = {i:0 for i,c in enumerate(refseq, 1)}
        line=ref.readline()
       
    inFile = open(inputFile, 'r')
    line = inFile.readline()
    while line != '':
        fields = line.split()
        gene = str(fields[3])   #gene
        readposition = int(fields[4])   #left-most position based on having 21 flanking nucleotides before 'A' of ATG
        readseq = str(fields[5])   #footprint seq
        readlength = len(readseq)      #footprint length
                
        if readlength == 25:    #select footprint read length of interest (e.g. 28mers)
            if gene in countsDict:
                if readposition in countsDict[gene]:              
                    countsDict[gene][readposition] = countsDict[gene][readposition] + 1
            else:
                countsDict[gene][readposition] = 1         
                       
        line = inFile.readline()

    outFile = open(outputFile, 'w')
    for G in sorted(countsDict.keys()) and sorted(refDict.keys()):
        for x in sorted(countsDict[G].keys()) and sorted(refDict[G].keys()):
            outFile.write(str(G) + '\t' + str(x-21) + '\t' + str(refDict[G][x]) + '\t' + str(countsDict[G][x]) + '\n') #An offset is introduced for flanking region. Position 1 corresponds to 'A' in 'ATG'

if __name__=='__main__':
    inputFile = '/Users/FrydmanLab/Documents/K_Stein/ProfilingData/KCSJF05/D1-2/D1-2_cds.map'
    outputFile = 'D1-2_25mer.density'
    refFile= '/Users/FrydmanLab/Documents/K_Stein/KilaueaBackup/ProfilingSoftware/bowtie_libraries/ce_proteincoding_21bp.fa'

    rawdata(inputFile, refFile, outputFile)
    