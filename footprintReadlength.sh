#!/bin/bash

# For each directory, determine the length distribution of sequencing reads
 
for dir in `ls -d */`;
	do
		echo $dir
	 	python readlength_distribution.py $dir${dir%/}.map /Users/FrydmanLab/Desktop/${dir%/}.csv
	done
