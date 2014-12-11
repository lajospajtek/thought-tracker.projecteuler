#
# ans: 4075

f = [1]
g = 1
for i in range(1,101):
  g *= i
  f.append(g)

res = 0
for n in range(2,101):
  for r in range(1,n+1):
    c = (f[n]/f[r])/f[n-r]
    #print n, r, c
    if c > 1000000: 
      res += 1

print "res =", res
