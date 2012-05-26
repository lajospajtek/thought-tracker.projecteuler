def is_pandigital(n):
  l = list(n)
  l.sort()
  return l == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def main():
  for n in range(9876, 9123, -1):
    m = str(n)+str(n*2)
    if is_pandigital(m):
      print m
      break

if __name__ == "__main__":
    main()

