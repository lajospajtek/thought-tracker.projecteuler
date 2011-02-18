import math

max_sum = -1

for a in range(90,100):
    p = 1
    for b in range(1,100):
	p *= a
	s = sum([int(c) for c in str(p)])
	if s > max_sum:
	    max_sum = s
	    #print a, b, max_sum

print max_sum

