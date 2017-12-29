inFile = open('datasets/rosalind_gc.txt').read().split('>')
counter = 0
results = 0


for i in range(0, len(inFile)):
	fasta = inFile[i][:14]
	base = list(inFile[i][14:])
	length = len(base)

	for j in range(0, length):
		if base[j] == "G":
			counter +=1
		if base[j] == "C":
			counter +=1
print counter		

