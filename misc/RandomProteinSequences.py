import random
import numpy as np
import linecache

#seq_lib = open("/Users/KevinStein/Desktop/Lab/Bioinformatics/ReferenceData/FastaSubsets/sc_proteins_RiboSeq_sequenceonly.fasta", "r")
seq_lib = open('/Users/KevinStein/Desktop/Lab/Bioinformatics/ReferenceData/FastaSubsets/Cele_protein_RiboSeq_sequenceonly.fa', 'r')
outputFile = open("/Users/KevinStein/Desktop/3mer_worm.csv", "w")
k = 11000
line = seq_lib.readline()
linecount = sum(1 for line in seq_lib)
seq_lib.seek(0)

random_linenos = np.random.choice(xrange(linecount), k)
for i in random_linenos:
    #line = linecache.getline("/Users/KevinStein/Desktop/Lab/Bioinformatics/ReferenceData/FastaSubsets/sc_proteins_RiboSeq_sequenceonly.fasta", i)
    line = linecache.getline("/Users/KevinStein/Desktop/Lab/Bioinformatics/ReferenceData/FastaSubsets/Cele_protein_RiboSeq_sequenceonly.fa", i)            
    protseq = str(line.strip())
    length = len(protseq)-1
    if length >= 50:            
        position = random.randint(3,length)
        #index1 = position - 10
        #index1 = position - 30
        index1 = position - 3
        seq = str(protseq[index1:position])
        outputFile.write(str(seq) + '\n')
        #outputFile.write(str('>') + '\n' + str(seq) + '\n')
    else:
        continue

seq_lib.close()
outputFile.close()