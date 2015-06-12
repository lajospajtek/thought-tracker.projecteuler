#
#
# Problem 85
#
# By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:
#
# Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with
# the nearest solution.
#
# ans: 2772


def sub_rectangles(x, y):
    return sum([(x-a)*(y-b) for b in range(0, y) for a in range(0, x)])


R = 2000000
rectangles = 2001000  # assuming it's close
area = 0
for x in range(2, 2001):
    for y in range(x, 2001):
        n = sub_rectangles(x, y)
        if abs(rectangles - R) > abs(n - R):
            rectangles = n
            area = x * y
            print x, y, n, area
        if n > R:
            break
    if x == y:
        break

print "ans:", area
