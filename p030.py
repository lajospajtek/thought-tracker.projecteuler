# Project Euler Problem 30

# Surprisingly there are only three numbers that can be written as the sum of 
# fourth powers of their digits:
#
#    1634 = 1^(4) + 6^(4) + 3^(4) + 4^(4)
#    8208 = 8^(4) + 2^(4) + 0^(4) + 8^(4)
#    9474 = 9^(4) + 4^(4) + 7^(4) + 4^(4)
#
# As 1 = 1^(4) is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth 
# powers of their digits.

# ans: 443839

def take_3():
  sum = 0
  for i in range(1000,1000000):
    j = i
    p = 0
    while j != 0:
      j, r = divmod(j,10)
      p += pow(r,5)
    if i == p:
      sum += i
      print i
  print sum

def take_2():
  sum=0
  rp = [(x,pow(x,5)) for x in range(0,10)]

  for i, ii in rp:
    for j, jj in rp:
      for k, kk in rp:
        for l, ll in rp:
          for m, mm in rp:
            for n, nn in rp:
              n1 = 100000*i+10000*j+1000*k+100*l+10*m+n
              n2 = ii + jj + kk + ll + mm + nn
              if n1 < 2: continue
              if n1 == n2: 
                sum += n1
                print i,j,k,l,m,n,n1
  print sum

def take_1():
  sum=0
  for i in range(1,10):
    for j in range(0,10):
      for k in range(0,10):
          n1 = 100*i+10*j+k
          n2 = pow(i,5)+pow(j,5)+pow(k,5)
          if n1 == n2: 
            sum += n1
            print i,j,k,n1

  for i in range(1,10):
    for j in range(0,10):
      for k in range(0,10):
        for l in range(0,10):
          n1 = 1000*i+100*j+10*k+l
          n2 = pow(i,5)+pow(j,5)+pow(k,5)+pow(l,5)
          if n1 == n2: 
            sum+=n1
            print i,j,k,l,n1

  for i in range(1,10):
    for j in range(0,10):
      for k in range(0,10):
        for l in range(0,10):
          for m in range(0,10):
            n1 = 10000*i+1000*j+100*k+10*l+m
            n2 = pow(i,5)+pow(j,5)+pow(k,5)+pow(l,5)+pow(m,5)
            if n1 == n2: 
              sum+=n1
              print i,j,k,l,m,n1

  for i in range(1,10):
    for j in range(0,10):
      for k in range(0,10):
        for l in range(0,10):
          for m in range(0,10):
            for n in range(0,10):
              n1 = 100000*i+10000*j+1000*k+100*l+10*m+n
              n2 = pow(i,5)+pow(j,5)+pow(k,5)+pow(l,5)+pow(m,5)+pow(n,5)
              if n1 == n2: 
                sum+=n1
                print i,j,k,l,m,n,n1

  print sum

if __name__=='__main__':
  from timeit import Timer
  t = Timer("take_1()", "from __main__ import take_1")
  print t.timeit(1)
  t = Timer("take_2()", "from __main__ import take_2")
  print t.timeit(1)
  t = Timer("take_3()", "from __main__ import take_3")
  print t.timeit(1)

