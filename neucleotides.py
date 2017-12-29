def nucleotides(n):
	A = 0
	G = 0
	C = 0
	T = 0
	string = map(str, n)

	for i in range(1,len(string)):
		if string[i] == "A":
			A+=1
		if string[i] == "G":
			G+=1
		if string[i] == "C":
			C+=1
		if string[i] == "T":
			T+=1	
	print A, C, G, T	


inFile = open("rosalind_dna.txt").read()
nucleotides(inFile)
