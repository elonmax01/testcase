#include <stdio.h>
#define K long
K int facto(K int n)
{
    K int fact=1;
    K int i;
    for(i=1;i<=n;i++)
    {
        fact=fact*i;
    }
    return fact;
}
int main() 
{
    K int k, s=0, n1, n2, n;
    K int t,i;
    scanf("%ld", &t);
    { s=0;
    scanf("%ld", &n);
    n1=n; n2=0;
    do {
        k=(facto((n1+n2)))/((facto(n1)*facto(n2)));
        s=s+k;
        n1=n1-2;
        n2++;
    } while (n1>=0);

    if (n==2)
        s=1;
    printf("%ld\n", s);
    }
    return 0;
}