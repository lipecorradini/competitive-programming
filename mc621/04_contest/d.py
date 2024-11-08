def getRemainder(n, p):
    ans = 0
    for number in sorted(p, reverse=True):
        ans = (ans * 10 + int(number)) % n
    print(ans)

def main():

    t = int(input())

    while(t>0):
        t -= 1
        n = int(input())
        p = input()
        getRemainder(n, p)
    return

main()