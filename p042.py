from math import sqrt

def is_triangle(t):
    d = sqrt(1+8*t)
    return (t%1 == 0) and (d%2 == 1)

f = open("words.txt", "r")
text = f.read()
names = text.split("\",\"")
names[0] = names[0][1:]
names[-1] = names[-1][:-1]
score = []
triangles = 0
for name in names:
    nv = 0
    for letter in name: nv += (ord(letter)-64)
    score.append(nv)
    t = is_triangle(nv)
    if t: triangles += 1
#    print name, nv, is_triangle(nv)
print "triangle words:", triangles
