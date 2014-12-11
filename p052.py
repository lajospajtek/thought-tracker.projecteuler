#
# ans: 142857

from math import log

x = 0
while True:
    x += 1
    x6 = 6*x
    if (x%1000) == 0:
	print x, int(log(x,10)), int(log(6*x,10))
    if int(log(x,10)) != int(log(x6,10)): continue
    s2 = str(2*x)
    s6 = str(6*x)
    ss2 = sorted(s2)
    ss6 = sorted(s6)
    if ss2 != ss6: continue
    ss3 = sorted(str(3*x))
    if ss2 != ss3: continue
    ss4 = sorted(str(4*x))
    if ss2 != ss4: continue
    ss5 = sorted(str(5*x))
    if ss2 != ss5: continue
    print x, 2*x, 3*x, 4*x, 5*x, 6*x
    break

