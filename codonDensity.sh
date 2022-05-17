#!/bin/bash

# Count reads at each nucleotide and sum up for each codon
# 
# Before using this script, update file nt_density.py after empirically determining the 
# length of reads to keep and the offset to use

for dir in `ls -d */`;
	do
		echo $dir
		echo "A-site nucleotide read density..."
	 	python nt_density_A.py $dir${dir%/}.map $dir${dir%/}_A.density /Users/FrydmanLab/Documents/K_Stein/KilaueaBackup/ProfilingSoftware/bowtie_libraries/Cele_cds_21bp_RiboSeq.fa ;
	 	echo "A-site codon read density..."
	 	python codon_density.py $dir${dir%/}_A.density $dir${dir%/}_A.codon
	 	echo "Compress intermediate files..."
	 	gzip $dir${dir%/}.map
	 	gzip $dir${dir%/}_norrna.fastq
	 	rm ${dir%/}/*.density
	done
