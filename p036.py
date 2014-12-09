
# ans: 872187

def palindromic(s):
    if s[-1] == '0': return False
    n = len(s) // 2 +1
    for i in range(0, n): 
	if s[i] != s[-i-1]: return False
    return True

s = 0
for i in range (1,1000000,2):
    if palindromic(str(i)) and palindromic(bin(i)[2:]):
        print i, bin(i)[2:]
        s += i	

print s

