#include <stdio.h>
#include <stdint.h>
#include <string.h>


typedef struct fact_exp_s {
  uint64_t factor;
  uint64_t exp;
} fact_exp_t;

typedef struct factors_s {
  unsigned count;
  fact_exp_t factors[128];
} factors_t;

int primefactors(uint64_t, factors_t*);
uint64_t gcd(uint64_t a, uint64_t b);
int is_achilles(factors_t *factors);
uint64_t totient(uint64_t n, const factors_t *factors, factors_t *tfactors);
void print_factors(const factors_t *factors);

int
main(int argc, char **argv)
{
  factors_t factors;
  factors_t tfactors;

  uint64_t n = 0;
  for (n=0; n<10000L; ++n) { 
    factors.count = 0;
    int rc = primefactors(n, &factors);
    if (rc != 0) continue;
    if (!is_achilles(&factors)) continue;
    uint64_t tot = totient(n, &factors, &tfactors);
    if (!is_achilles(&tfactors)) continue;
    printf("%llu: ", n); 
    print_factors(&factors);
    printf(" tot=%llu: ", tot);
    print_factors(&tfactors);
    printf("\n");
  }
  return 0;
}

void
print_factors(const factors_t *factors)
{
  int i;
  const fact_exp_t *fp = factors->factors;
  for(i=0; i<factors->count; ++i, ++fp) {
    printf("%llu^%llu, ", fp->factor, fp->exp);
  }
}

uint64_t 
totient(uint64_t n, const factors_t *factors, factors_t *tfactors)
{
  memcpy(tfactors, factors, sizeof(factors_t));
  uint64_t tot = n, tres = 1;
  fact_exp_t *fe = tfactors->factors;
  unsigned int i = tfactors->count;
  while (i > 0) {
    --(fe->exp);
    tres *= fe->factor-1;
    //tot *= fe->factor-1;
    tot /= fe->factor;
    --i;
    ++fe;
  }
  primefactors(tres, tfactors);
  return tot*tres;
}

uint64_t
gcd(uint64_t a, uint64_t b)
{
  uint64_t t;
  while (b != 0L) {
    t = b;
    b = a % b;
    a = t;
  }
  return a;
}

int
is_achilles(factors_t *factors)
{
  uint64_t g = 1L;
  fact_exp_t *fe = &(factors->factors[0]);
  if (factors->count <= 1) return 0;
  else {
    g = fe->exp;
    uint64_t i = factors->count;
    --i;
    ++fe;
    while (i > 0) {
      if (fe->exp == 1) return 0;
      g = gcd(g, fe->exp);
      ++fe;
      --i;
    }
  }
  return g == 1L;  
}

void 
add_factor_old(factors_t *factors, uint64_t f, unsigned e)
{
  fact_exp_t *fe = &(factors->factors[factors->count]);
  if (factors->count == 0) {
    fe->factor = f;
    fe->exp = e;
    factors->count = 1;
  } else {
    if ((fe-1)->factor == f) {
      (fe-1)->exp += e;
    } else {
      fe->factor = f;
      fe->exp = e;
      ++(factors->count);
    }
  } 
}

void 
add_factor(factors_t *factors, uint64_t f, unsigned e)
{
  fact_exp_t *fe = factors->factors;
  if (factors->count == 0) {
    fe->factor = f;
    fe->exp = e;
    factors->count = 1;
  } else {
    unsigned i = factors->count;
    while (i>0) {
      if (fe->factor == f) {
        fe->exp += e;
        break;
      }
    --i;
    ++fe;
    }
    if (i==0) {
      fe->factor = f;
      fe->exp = e;
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
      add_factor(factors, loop, 1);
      ++exp;
    } else {
      if (exp == 1) return -1;
      exp = 0;
      ++loop;
    }
  }
  if (exp < 3) return -1;
  return 0;
}
