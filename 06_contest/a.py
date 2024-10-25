# algorithm largely based on https://stackoverflow.com/questions/27336269/how-to-optimize-factorization-code-in-python

def factors(n):
    fs = []

    # remove 2
    while n % 2 == 0:
        fs.append(2)
        n //= 2
    
    # now deal odds
    f = 3
    while f * f <= n:
        while n % f == 0:
            fs.append(f)
            n //= f
        f += 2 
    if n > 1:
        fs.append(n)
    return fs



def main():
    
    while True:
        n = int(input())
        if n == 0: return

        factor = factors(n)
        
        if not factor:
            print()
            continue

        factor_counts = {}
        for exp in factor:
            factor_counts[exp] = factor_counts.get(exp, 0) + 1

        output = ' '.join([f"{int(prime)}^{count}" for prime, count in sorted(factor_counts.items())])
        print(output)

main()

