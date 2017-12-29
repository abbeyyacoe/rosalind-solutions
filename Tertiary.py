def Teritary(n):
	string = map(str, n[::-1].split(' '))
	for i in range(0,len(string)):
		if string[i] == "A":
			string[i] == "T"
		if string[i] == "T":
			string[i] == "A"
		if string[i] == "C":
			string[i] == "G"
		if string[i] == "G":
			string[i] == "C"		
	print "".join(string)
Teritary('AAAACCCGGT')