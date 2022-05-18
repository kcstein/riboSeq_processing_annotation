#fasta = open('/Users/KevinStein/Desktop/Lab/Bioinformatics/ReferenceData/FastaSubsets/Cele_protein_RiboSeq.fa', 'r')
#fasta = open('/Users/KevinStein/Desktop/Lab/Bioinformatics/ReferenceData/FastaSubsets/Scer_protein_RiboSeq.fa', 'r')
fasta = open('/Users/KevinStein/Desktop/stallNOTkenyon_aggregates.fa', 'r')
csv_out = open("/Users/KevinStein/Desktop/stallNOTkenyon_aggregates_AAcomposition.csv", "w")


for line in fasta:
    if line.startswith(">"):
	#continue
	geneb = str(line[1:len(line)])
	gene = geneb.strip()
	#print str(line)
    else:
        length = len(line.strip())
        start = int(0)
        #start = int(58) # 58 to 62 for active site; 0 to 25 for nascent
        #print line[0]
        #end = int(62)
        end = int(length)
        #print line[25]
        search_length = int(end - start - 1) # -1 if file has asterisks
        a = "A"
        c = "C"
        d = "D"
        e = "E"
        f = "F"
        g = "G"
        h = "H"
        i = "I"
        k = "K"
        l = "L"
        m = "M"
        n = "N"
        p = "P"
        q = "Q"
        r = "R"
        s = "S"
        t = "T"
        v = "V"
        w = "W"
        y = "Y"
	count_a = line.count(a, start, end)
#	percent_a = 100 * float(count_a) / float(search_length)
	percent_a = float(count_a) / float(search_length)
	count_c = line.count(c, start, end) 
#	percent_c = 100 * float(count_c) / float(search_length)
	percent_c = float(count_c) / float(search_length)
	count_d = line.count(d, start, end) 
#	percent_d = 100 * float(count_d) / float(search_length)
	percent_d = float(count_d) / float(search_length)
	count_e = line.count(e, start, end) 
#	percent_e = 100 * float(count_e) / float(search_length)
	percent_e = float(count_e) / float(search_length)
	count_f = line.count(f, start, end) 
#	percent_f = 100 * float(count_f) / float(search_length)
	percent_f = float(count_f) / float(search_length)
	count_g = line.count(g, start, end) 
#	percent_g = 100 * float(count_g) / float(search_length)
	percent_g = float(count_g) / float(search_length)
	count_h = line.count(h, start, end) 
#	percent_h = 100 * float(count_h) / float(search_length)
	percent_h = float(count_h) / float(search_length)
	count_i = line.count(i, start, end)
#	percent_i = 100 * float(count_i) / float(search_length)
	percent_i = float(count_i) / float(search_length)
	count_k = line.count(k, start, end) 
#	percent_k = 100 * float(count_k) / float(search_length)
	percent_k = float(count_k) / float(search_length)
	count_l = line.count(l, start, end) 
#	percent_l = 100 * float(count_l) / float(search_length)
	percent_l = float(count_l) / float(search_length)
	count_m = line.count(m, start, end) 
#	percent_m = 100 * float(count_m) / float(search_length)
	percent_m = float(count_m) / float(search_length)
	count_n = line.count(n, start, end) 
#	percent_n = 100 * float(count_n) / float(search_length)
	percent_n = float(count_n) / float(search_length)
	count_p = line.count(p, start, end) 
#	percent_p = 100 * float(count_p) / float(search_length)
	percent_p = float(count_p) / float(search_length)
	count_q = line.count(q, start, end) 
#	percent_q = 100 * float(count_q) / float(search_length)
	percent_q = float(count_q) / float(search_length)
	count_r = line.count(r, start, end) 
#	percent_r = 100 * float(count_r) / float(search_length)
	percent_r = float(count_r) / float(search_length)
	count_s = line.count(s, start, end) 
#	percent_s = 100 * float(count_s) / float(search_length)
	percent_s =  float(count_s) / float(search_length)
	count_t = line.count(t, start, end) 
#	percent_t = 100 * float(count_t) / float(search_length)
	percent_t = float(count_t) / float(search_length)
	count_v = line.count(v, start, end) 
#	percent_v = 100 * float(count_v) / float(search_length)
	percent_v = float(count_v) / float(search_length)
	count_w = line.count(w, start, end) 
#	percent_w = 100 * float(count_w) / float(search_length)
	percent_w = float(count_w) / float(search_length)
	count_y = line.count(y, start, end) 
#	percent_y = 100 * float(count_y) / float(search_length)
	percent_y = float(count_y) / float(search_length)
        csv_out.write(str(gene) + ',')
        csv_out.write(str(percent_a) + ',')
        csv_out.write(str(percent_c) + ',')
        csv_out.write(str(percent_d) + ',')
        csv_out.write(str(percent_e) + ',')
        csv_out.write(str(percent_f) + ',')
        csv_out.write(str(percent_g) + ',')
        csv_out.write(str(percent_h) + ',')
        csv_out.write(str(percent_i) + ',')
        csv_out.write(str(percent_k) + ',')
        csv_out.write(str(percent_l) + ',')
        csv_out.write(str(percent_m) + ',')
        csv_out.write(str(percent_n) + ',')
        csv_out.write(str(percent_p) + ',')
        csv_out.write(str(percent_q) + ',')
        csv_out.write(str(percent_r) + ',')
        csv_out.write(str(percent_s) + ',')
        csv_out.write(str(percent_t) + ',')
        csv_out.write(str(percent_v) + ',')
        csv_out.write(str(percent_w) + ',')
        csv_out.write(str(percent_y) + '\n')

#csv_out.write(percent_a + ',' + percent_b)

fasta.close()
csv_out.close()   