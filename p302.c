#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

typedef struct fact_exp_s {
  uint64_t factor;
  uint64_t exp;
} fact_exp_t;

typedef struct factors_s {
  unsigned count;
  fact_exp_t factors[128];
} factors_t;

int add_primefactors(uint64_t, factors_t*);
int add_primefactors_break(uint64_t, factors_t*);
uint64_t gcd(uint64_t a, uint64_t b);
int is_achilles(factors_t *factors);
uint64_t totient(uint64_t n, const factors_t *factors, factors_t *tfactors);
void print_factors(const factors_t *factors);
void generate_primes(uint64_t **primes, unsigned *siz, uint64_t limit);

static uint64_t limit = 100000000LL;
uint64_t *primes = NULL;
unsigned psiz;

int
main(int argc, char **argv)
{
  factors_t factors;
  factors_t tfactors;

  generate_primes(&primes, &psiz, pow(limit, 1.0/3.0));
  printf("primes: %u\n", psiz);
//  for (j=0; j<siz; ++j) {
//    printf("%7llu", primes[j]);
//    if (j%10==9) printf("\n");
//  }
//  printf("\n");

  uint64_t n = 0;
  unsigned co = 0;
  for (n=0; n<limit; ++n) { 
    factors.count = 0;
    int rc = add_primefactors_break(n, &factors);
    if (rc != 0) continue;
    if (!is_achilles(&factors)) continue;
    uint64_t tot = totient(n, &factors, &tfactors);
    if (!is_achilles(&tfactors)) continue;
    printf("%u: %llu: ", ++co, n); 
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
  add_primefactors(tres, tfactors);
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
    if (g == 1) return 0;
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
add_factor_last(factors_t *factors, uint64_t f, unsigned e)
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
    int i = factors->count;
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
add_primefactors(uint64_t n, factors_t *factors)
{
  unsigned exp = 0;
  unsigned j = 0;
  while (primes[j] <= n && j < psiz) {
    if (n % primes[j] == 0) {
      n /= primes[j];
      add_factor(factors, primes[j], 1);
      ++exp;
    } else {
      exp = 0;
      ++j;
    }
  }
  return 0;
}

int 
add_primefactors_break(uint64_t n, factors_t *factors)
{
  unsigned exp = 0;
  unsigned j = 0;
  while (primes[j] <= n && j < psiz) {
    exp = 0;
    while (n % primes[j] == 0) {
      n /= primes[j];
      ++exp;
    } 
    if (exp == 1) return -1;
    if (exp != 0) add_factor_last(factors, primes[j], exp);
    ++j;
  }
  if (exp < 3) return -1;
  return 0;
}

void
generate_primes(uint64_t **primes, unsigned *size, uint64_t limit)
{
  unsigned msiz = 1.2*limit/log(limit);
  uint64_t *p = (uint64_t *)malloc(msiz*sizeof(uint64_t));
  *primes = p;
  p[0] = 2;
  p[1] = 3;
  unsigned i = 2;
  uint64_t q = 5;
  while (q < limit) {
    unsigned l = sqrt(q);
    unsigned j = 0, intr = 0;
    while (p[j] <= l) {
      if (q % p[j++] == 0) {
       intr = 1; 
       break;
       }
    }
    if (!intr) {
      p[i++] = q;
    }
    q += 2;
  }
  *size = i;
}
