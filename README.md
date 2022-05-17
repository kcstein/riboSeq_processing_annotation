# riboSeq_processing_annotation

This repository contains the relevant scripts for the primary processing of RiboSeq data, along with annotation files that may be useful for downstream secondary analysis of data produced in *S. cerevisiae* or *C. elegans*.

**preprocessing.sh:** Process RiboSeq demultiplexed FASTQ files by trimming adapters, removing 5' nucleotide, removing rRNAs, and mapping to library of protein coding sequences.

**footprintReadlength.sh:** Assess distribution of read length using readlength_distribution.py. For relevant read lengths, use derivative of 25mer_alignment.py to sum reads at each nucleotide and empirically determine offset to assign ribosome protected fragments to the first nucleotide of the A-site within the ribosome's active site.

**codonDensity.sh:** After calculating offset, sum reads at each nucleotide using nt_density_A.py, now aligned at the ribosome's A-site, followed by summing nucleotide counts for each codon using codon_density.py.


## Directories:

**bowtie_reference:** Contains reference FASTA files to create custom bowtie libraries for alignment RiboSeq data.

**annotation:** Contains relevant files for secondary analysis, including annotation of the S. cerevisiae and C. elegans proteomes.
