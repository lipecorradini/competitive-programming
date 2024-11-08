#include <iostream>
#include <unordered_map>
#include <cmath>
#include <bits/stdc++.h>

using namespace std;
// algrithm largely based on https://www.rookieslab.com/posts/fastest-way-to-check-if-a-number-is-prime-or-not
// and on https://www.geeksforgeeks.org/pollards-rho-algorithm-prime-factorization/
// and https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/

std::unordered_map<long long, long long> factors;

int k = 7;

long long power(long long x, unsigned int y, long long p)
{
    long long res = 1;
    x = x % p;
    while (y > 0)
    {
        if (y & 1)
            res = (__int128(res) * x) % p;
        y = y >> 1;
        x = (__int128(x) * x) % p;
    }
    return res;
}
 
bool miillerTest(long long d, long long n)
{
    // Pick a random number in [2..n-2]
    // Corner cases make sure that n > 4
    long long a = 2 + rand() % (n - 4);
 
    // Compute a^d % n
    long long x = power(a, d, n);
 
    if (x == 1  || x == n-1)
       return true;
 
    // Keep squaring x while one of the following doesn't
    // happen
    // (i)   d does not reach n-1
    // (ii)  (x^2) % n is not 1
    // (iii) (x^2) % n is not n-1
    while (d != n-1)
    {
        x = (x * x) % n;
        d *= 2;
 
        if (x == 1)      return false;
        if (x == n-1)    return true;
    }
 
    // Return composite
    return false;
}
 
// It returns false if n is composite and returns true if n
// is probably prime.  k is an input parameter that determines
// accuracy level. Higher value of k indicates more accuracy.
bool isPrime(long long n, long long k)
{
    // Corner cases
    if (n <= 1 || n == 4)  return false;
    if (n <= 3) return true;
 
    // Find r such that n = 2^d * r + 1 for some r >= 1
    long long d = n - 1;
    while (d % 2 == 0)
        d /= 2;
 
    // Iterate given number of 'k' times
    for (long long i = 0; i < k; i++)
         if (!miillerTest(d, n))
              return false;
 
    return true;
}
 

long long mod_mul(long long a, long long b, long long mod) {
    long long result = 0;
    a %= mod;
    while (b) {
        if (b & 1) result = (result + a) % mod;
        a = (a * 2) % mod;
        b >>= 1;
    }
    return result;
}


long long int PollardRho(long long int n)
{
    srand (time(NULL));

    if (n==1) return n;

    if (n % 2 == 0) return 2;

    long long int x = (rand()%(n-2))+2;
    long long int y = x;
    long long int c = (rand()%(n-1))+1;

    long long int d = 1;  

    while (d==1)
    {
        x = (mod_mul(x, 2, n) + c + n)%n;

        y = (mod_mul(y, 2, n) + c + n)%n;
        y = (mod_mul(y, 2, n) + c + n)%n;

        d = __gcd(abs(x-y), n);

        if (d==n) return PollardRho(n);
    }

    return d;
}

void factorize(long long n) 
{
    if(n == 1)
        return;

    if(isPrime(n, k))      
    {
        factors[n]++;
        return;
    }
    long long divisor = PollardRho(n);  
    factorize(divisor);
    factorize(n/divisor);
}

int main() {
    while (true) {
        long long n;
        cin >> n;
        if (n == 0)
            return 0;

        factors.clear();

        factorize(n);

        for (const auto& exp : factors) {
            cout << exp.first << "^" << exp.second << " ";
        }
        cout << endl;
    }

    return 0;
}
