#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define MAX 10000u

uint64_t
reverse(uint64_t u)
{
  uint64_t digits[100];
  uint64_t c = 0;
  uint64_t i = u;
  while (i!=0) {
    uint64_t d = i % 10u;
    i /= 10u;
    digits[c++] = d;
  }
  uint64_t v = 1u;
  for (v=0,i=0; i<c; ++i) {
    v *= 10;
    v += digits[i];
  }
  return v;
}

uint64_t
palindrome2(uint64_t u, uint64_t r)
{
  while (u!=0 && r!=0) {
    uint64_t d = u % 10;
    uint64_t e = r % 10;
    if (e != d) return 0;
    u /= 10u;
    r /= 10u;
  }
  return 1;
}

uint64_t
palindrome(uint64_t u)
{
  uint64_t digits[100];
  uint64_t c = 0;
  uint64_t i = u;
  while (i!=0) {
    uint64_t d = i % 10u;
    i /= 10u;
    digits[c++] = d;
  }
  int j = c-1;
  i = 0;
  uint64_t v = 1u;
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
  uint64_t* cdd = calloc(sizeof(uint64_t), MAX);

  int i, ctr = 1;
  for(i=1; i<MAX; ++i) {
    if (cdd[i] == 0) {
     /* if (i%10==0) {
        ++cdd[i];
        continue;
      }*/
      int z;
      uint64_t d = i;
      for (z=0; z<50; ++z) {
        uint64_t r = reverse(d);
        uint64_t sum = r+d;
        uint64_t p = palindrome(sum);
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
