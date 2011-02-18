limit = 1000
s = 0
a = []
n = 1
while n<limit:
	if (n%3)==0 or ((n%5)==0):
		s +=n
		a.append(n)
	n+=1

a.sort()
print "len:", len(a)
print "sum:", sum(a)
print "sum:", s
#text = raw_input('press enter')

# pencil-and-paper solution:
# sum of multipliers of 3, below 1000: 3 * (333*(333+1))/2
# sum of multipliers of 5, below 1000: 5 * (199*200)/2
# minus the sum of multipliers of 15, below 1000: 15 * (66*67)/2

