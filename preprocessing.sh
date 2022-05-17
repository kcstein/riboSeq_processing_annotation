#!/bin/bash

# Initial processing of RiboSeq data:
# 1. Remove adapter using Cutadapt
# 2. Trim first nucleotide using FastX_toolkit
# 3. Remove noncoding RNA using bowtie library of interest
# 4. Align reads to genome using Bowtie
 
for file in *.fastq.gz;
	do
		echo ${file%.fastq.gz}
		echo "Unzip..."
		gunzip $file
		echo "Cutting adapters..."
		# Change adapter sequence as necessary after the "-a" flag
		python /Users/FrydmanLab/Documents/K_Stein/KilaueaBackup/ProfilingSoftware/cutadapt2/bin/cutadapt -f fastq -a AGATCGGAAGAGC -O 6 -m 6 -o ${file%.fastq.gz}_cut.fastq -n 3 -e 0.15 --discard-untrimmed ${file%.fastq.gz}.fastq ;
		rm ${file%.fastq.gz}.fastq
		echo "Trimming..."
		fastx_trimmer -Q33 -f 2 -i ${file%.fastq.gz}_cut.fastq -o ${file%.fastq.gz}_trimmed.fastq ;
		rm ${file%.fastq.gz}_cut.fastq ;
		echo "Removing rRNA..."
		# Change name and location of rRNA Bowtie library as necessary
		bowtie --un ${file%.fastq.gz}_norrna.fastq /Users/FrydmanLab/Documents/K_Stein/KilaueaBackup/ProfilingSoftware/bowtie_libraries/Cele_rRNA ${file%.fastq.gz}_trimmed.fastq > /dev/null ;
		rm ${file%.fastq.gz}_trimmed.fastq ; 
		echo "Bowtie alignment..."
		# Change name and location of Bowtie library as necessary
		bowtie -y -a -m 1 -v 2 --norc --best --strata /Users/FrydmanLab/Documents/K_Stein/KilaueaBackup/ProfilingSoftware/bowtie_libraries/Cele_cds_21bp_RiboSeq ${file%.fastq.gz}_norrna.fastq ${file%.fastq.gz}.map
		rm ${file%.fastq.gz}.fastq
	done