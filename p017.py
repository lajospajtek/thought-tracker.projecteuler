# p017
# http://www.mathblog.dk/project-euler-17-letters-in-the-numbers-1-1000/

ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
ones_count = map(len, ones)

tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
tens_count = map(len, tens)

def tens_ones_count(m):
    if m < 21:
        return ones_count[m]
    else:
        return tens_count[m/10] + ones_count[m%10]

sum = 0
for n in range(1,1000):
    (d, m) = divmod(n, 100)
    sum0 = tens_ones_count(m)
    if d > 0:
        if m > 0: 
            sum += 3 # 'and'
        sum0 += 7 # 'hundred'
        sum0 += ones_count[d]
    sum += sum0

sum += 11 # for "one thousand"
print sum 

