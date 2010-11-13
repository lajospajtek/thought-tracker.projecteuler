#include <stdio.h>
#include <stdint.h>


typedef struct fact_exp_s {
  uint64_t factor;
  uint64_t exp;
} fact_exp_t;

typedef struct factors_s {
  unsigned count;
  fact_exp_t factors[128];
} factors_t;

int primefactors(uint64_t, factors_t*);

int
main(int argc, char **argv)
{
  factors_t factors;

  uint64_t n = 0;
  for (n=0; n<100000000L; ++n) { 
    factors.count = 0;
    int rc = primefactors(n, &factors);
    if (rc != 0) continue;

    printf("%llu: ", n); 
    int i;
    fact_exp_t *fp = factors.factors; 
    for(i=0; i<factors.count; ++i, ++fp) {
      printf("%llu^%llu, ", fp->factor, fp->exp);
    }
    printf("\n");
  }
  return 0;
}

void 
add_factor(factors_t *factors, uint64_t f)
{
  fact_exp_t *fe = &(factors->factors[factors->count]);
  if (factors->count == 0) {
    fe->factor = f;
    fe->exp = 1;
    factors->count = 1;
  } else {
    if ((fe-1)->factor == f) {
      ++((fe-1)->exp);
    } else {
      fe->factor = f;
      fe->exp = 1;
      ++(factors->count);
    }
  } 
}

int 
primefactors(uint64_t n, factors_t *factors)
{
  uint64_t loop = 2;
  unsigned exp = 0;
  while (loop <= n) {
    if (n % loop == 0) {
      n /= loop;
      add_factor(factors, loop);
      ++exp;
    } else {
      if (exp == 1) return -1;
      exp = 0;
      ++loop;
    }
  }
  if (exp == 1) return -1;
  return 0;
}
