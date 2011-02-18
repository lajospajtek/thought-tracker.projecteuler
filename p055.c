#include <stdio.h>
#include <stdlib.h>

#define MAX 10000u

unsigned
reverse(unsigned u)
{
  unsigned digits[10];
  unsigned c = 0;
  unsigned i = u;
  while (i!=0) {
    unsigned d = i % 10u;
    i /= 10u;
    digits[c++] = d;
  }
  unsigned v = 1u;
  for (v=0,i=0; i<c; ++i) {
    v *= 10;
    v += digits[i];
  }
  return v;
}

unsigned
palindrome2(unsigned u, unsigned r)
{
  while (u!=0 && r!=0) {
    unsigned d = u % 10;
    unsigned e = r % 10;
    if (e != d) return 0;
    u /= 10u;
    r /= 10u;
  }
  return 1;
}

unsigned
palindrome(unsigned u)
{
  unsigned digits[10];
  unsigned c = 0;
  unsigned i = u;
  while (i!=0) {
    unsigned d = i % 10u;
    i /= 10u;
    digits[c++] = d;
  }
  int j = c-1;
  i = 0;
  unsigned v = 1u;
  while (i<j) {
    if (digits[i] != digits[j]) {
      v = 0;
      break;
    }
    ++i;
    --j;
  }
  if (v!=0) {
    for (v=0,i=0; i<c; ++i) {
      v *= 10;
      v += digits[i];
    }
  }
  return v;
}

int
main (int arcv, char** argv)
{
  unsigned* cdd = calloc(sizeof(unsigned), MAX);

  int i, ctr = 1;
  for(i=0; i<MAX; ++i) {
    if (cdd[i] == 0) {
     /* if (i%10==0) {
        ++cdd[i];
        continue;
      }*/
      int z, d = i;
      for (z=0; z<50; ++z) {
        unsigned r = reverse(d);
        unsigned sum = r+d;
        unsigned p = palindrome(sum);
        if (p) break;
        d = sum;
      }
      if (z==50) {
        printf ("%6d: %d\n", ctr++, i);
      }
      //printf("%d  --> %d, %d\n", i, r, p);
    }
  }
  return 0;
}
