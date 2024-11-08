
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def gcdExtended(a, b):

    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y

def main():
    a, b, c = [int(x) for x in input().split()]

    # gcd(a, b) precisa dividir -c para que se tenha solucao

    max_divisor = gcd(a, b)

    if a == 0:
        val = (c * (-1)) % b 
        if val != 0:
            print(-1)
        else:
            print(f"0 {-1 * c // b}")
    
    elif b == 0:
        val = (c * (-1)) % a 
        if val != 0:
            print(-1)
        else:
            print(f"{-1 * c // a} 0")
    
    elif c % max_divisor != 0:
        print(-1)
    
    else: # extended euclidean algorithm to find a solution
        great, x, y = gcdExtended(a, b)
        x *= -1 * c
        x //= great

        y *= -1 * c
        y //= great

        # print(max_divisor)
        # print(x, y)


        if abs(x) > 5e18 or abs(y) > 5e18:
            print(-1)
        
        else:
            print(f"{int(x)} {int(y)}")

main()

    
    

    
