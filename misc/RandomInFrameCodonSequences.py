import random
import numpy as np
import linecache

seq_lib = open("/Users/KevinStein/Desktop/Lab/Bioinformatics/ReferenceData/FastaSubsets/sc_cds_21bp_nodubious_nooverlap_RiboSeq_sequenceonly.fasta", "r")
outputFile = open("/Users/KevinStein/Desktop/9mer_codons.csv", "w")
k = 10100
line = seq_lib.readline()
linecount = sum(1 for line in seq_lib)
seq_lib.seek(0)

random_linenos = np.random.choice(xrange(linecount), k)
for i in random_linenos:
    line = linecache.getline("/Users/KevinStein/Desktop/Lab/Bioinformatics/ReferenceData/FastaSubsets/sc_cds_21bp_nodubious_nooverlap_RiboSeq_sequenceonly.fasta", i)      
    cds = str(line.strip())
    length = len(cds)-51 #subtracting flanking 21bp 5' and 3' and stop codon and upstream 2 codons         
    if length >= 110:     
        position = random.randint(110,length) # first available position to choose is nucleotide 90 (codon 30)       
        if (position % 3 == 0):
            index1 = position + 27
            seq = str(cds[position:index1])
            outputFile.write(str(seq) + '\n')
        if (position % 3 == 1):
            position = position - 1
            index1 = position + 27
            seq = str(cds[position:index1])
            outputFile.write(str(seq) + '\n')
        if (position % 3 == 2):
            position = position - 2
            index1 = position + 27
            seq = str(cds[position:index1])
            outputFile.write(str(seq) + '\n')
    else:
        continue
        
seq_lib.close()
outputFile.close()