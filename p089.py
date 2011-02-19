rd = dict(M=1000, D=500, C=100, L=50, X=10, V=5, I=1)

file = open('roman.txt')
for line in file:
  num = line.rstrip()
  prev_val = 1001
  for ch in num:
    if prev_val < rd[ch]:
      print 'DESC', num
      break
  val = 0
  for ch in num:
    val += rd[ch]
  print num, "=", val

file.close()



