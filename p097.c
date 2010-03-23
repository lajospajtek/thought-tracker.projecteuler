#include<stdio.h>

int
main() 
{
	unsigned long long exp = 7830457;
	unsigned long long m = 1;
	int i;
	for (i=0; i<exp; ++i) {
		m *= 2; m%=10000000000ull;
	}
	m *= 28433;
	m++;
	m %= 10000000000ull;
	printf("[%llu]\n",  m);

}

