def mutations(s,t):
	s.split()
	t.split()
	count = 0
	for i in range(0, len(s)):
		if s[i] !== t[i]:
			count += 1	
	print count


data1 = 'GAGCCTACTAACGGGAT'
data2 = 'CATCGTAATGACGGCCT'
mutations(data1,data2)

