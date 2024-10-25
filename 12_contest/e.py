def cross(t1, t2):
    return t1[0]*t2[1] - t1[1]*t2[0]

def sub(p, s):
    return (p[0] - s[0], p[1] - s[1])
def main():
    t = int(input())

    for _ in range(t):
        x1, y1, x2, y2, x3, y3 = [int(x) for x in input().split()]
        
        t1 = (x1, y1)
        t2 = (x2, y2)
        p = (x3,  y3)

        ans = cross(sub(p, t1), sub(p, t2))

        if ans > 0:
            print("LEFT")
        elif ans == 0:
            print("TOUCH")
        else:
            print("RIGHT")

main()