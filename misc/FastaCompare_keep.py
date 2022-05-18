ids = []

fasta_ref = open("/Users/KevinStein/Desktop/Lab/Bioinformatics/ProfilingSoftware/bowtie_libraries/Scer_cds_21bp_nodubious_nooverlap_RiboSeq.fa", "r")
for line in fasta_ref:
	if line.startswith(">"):
            ids.append(line)
fasta_ref.close()

fasta1 = open("/Users/KevinStein/Desktop/shortened.fa", "r")
fasta_out = open("/Users/KevinStein/Desktop/shortened_subset.fa", "w")

flag = 0
for line in fasta1:
	if line.startswith(">"):
		if line in ids:
			fasta_out.write(line)
			flag = 1
		else:
			flag = 0
	elif flag:
		fasta_out.write(line)
fasta1.close()
fasta_out.close()