import csv

refDict = {}
#fasta = open("/Users/KevinStein/Desktop/Lab/Bioinformatics/ReferenceData/FastaSubsets/sc_cds_21bp_nodubious_nooverlap_RiboSeq.fasta", "r")
#fasta = open("/Users/KevinStein/Desktop/Lab/Bioinformatics/ReferenceData/FastaSubsets/Scer_protein_RiboSeq.fa", "r")
fasta = open("/Users/KevinStein/Desktop/Lab/Bioinformatics/ReferenceData/FastaSubsets/Cele_protein_RiboSeq.fa", "r")
line=fasta.readline()
while line != "":
    refgeneb = str(line[1:len(line)])
    refgene = refgeneb.strip()
    line=fasta.readline()
    refseq = str(line.strip())
    refDict[refgene] = refseq
    line=fasta.readline()
fasta.close()

outputFile = open("/Users/KevinStein/Desktop/stalls_seq.csv", "w")
#with open("/Users/KevinStein/Desktop/D_max.csv","rU") as inputFile:
with open("/Users/KevinStein/Desktop/Lab/Lab_notebook/1_Aging/RiboSeq_Analysis/Worm/doc/Fishers/stalling_peaks_seq.csv","rU") as inputFile:
#with open("/Users/KevinStein/Desktop/Lab/Lab_notebook/1_Aging/RiboSeq_Analysis/Chronological/doc/Fishers/sch9_stalls_60mer_seq.csv","rU") as inputFile:
    reader = csv.reader(inputFile, delimiter = ',')
    for row in reader:
            gene = str(row[0])
            #log = float(row[1])
            #pvalue = float(row[2])
            #padj = float(row[3])
            #pause_start = int(row[1])
            #pause_end = int(row[2])
            pauseposition = int(row[1])
            #Z = float(row[4])
            name = str(row[2])
            #pauseposition = pauseposition * 3 + 21 # for codons accounting for flanking sequence to convert to nucleotide position and taking EP sites upstream of peak site
            #index5 = int(pauseposition) - 13
            #index3 = int(pauseposition) + 0
            index5 = int(pauseposition) - 30 # for proteins
            index3 = int(pauseposition) + 0 # for proteins
            if gene in refDict:
	        refseq1 = refDict[gene]
	        #seq = str(refseq1) # take full sequence
	        #end = int(len(refseq1) - 1)
	        #seq = str(refseq1[0:end]) # full sequence minus asterisk
	        #length1 = int(len(refseq1))
	        seq = str(refseq1[index5:index3]) # for proteins
      	        #seq = str(refseq1[pauseposition:index3]) # for codons
      	        #if index3 < length1 and index5 > 0:
      	         #   seq = str(refseq1[index5:index3]) # custom
      	        #if index3 > length1:
      	         #   length2 = length1-1
      	          #  seq = str(refseq1[index5:length2])
      	        #if index5 < 0:
      	         #   seq = str(refseq1[1:index3])
      	        #outputFile.write(str('>') + str(gene) + '\n' + str(seq) + '\n')
   	        #outputFile.write(str(gene) + '\t' + str(log) + '\t' + str(pvalue) + '\t' + str(padj) + '\t' + str(seq) + '\n')
      	        #outputFile.write(str(gene) + " N N 7 298 0.1 " + str(seq) + '\n') # for TANGO
      	        #outputFile.write(str(gene) + '\t' + str(name) + '\t' + str(pauseposition) + '\t' + str(seq) + '\n') # for proteins
	        if seq.find("*") == -1:
	            #outputFile.write(str(gene) + ',' + str(name) + ',' + str(pauseposition) + ',' + str(seq) + '\n') # for proteins
	            if pauseposition > 30:
                        outputFile.write(str(gene) + ',' + str(name) + ',' + str(pauseposition) + ',' + str(seq) + '\n') # for proteins
		        #outputFile.write(str(gene) + '\t' + str(name) + '\t' + str(pauseposition - 21) + '\t' + str(seq) + '\n') # for codons
                        #outputFile.write(str(gene) + '\t' + str(pauseposition) + '\t' + str(seq) + '\n')
                        #outputFile.write(str('>') + str(gene) + '\n' + str(seq) + '\n')
                        #outputFile.write(str('>') + str(name) + '\t' + str(gene) + '\n' + str(seq) + '\n')
                        #outputFile.write(str(gene) + '\t' + str(name) + '\t' + str(seq) + '\n')
inputFile.close()
outputFile.close()

