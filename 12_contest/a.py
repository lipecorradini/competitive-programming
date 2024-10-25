t = int(input())

print("INTERSECTING LINES OUTPUT")
for _ in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = [int(x) for x in input().split()]
    
    if x2 == x1:

        if x3 == x4:
            if x3 == x2:
                print("LINE") # iguais
            else:
                print("NONE")
        else:
            a2 = (y4 - y3)/(x4 - x3)
            b2 = y3 - a2 * x3

            x_int = x1
            y_int = a2 * x_int + b2
            print(f"POINT {x_int:.2f} {y_int:.2f}")

    else:
        a1 = (y2 - y1)/(x2 - x1)
        b1 = y1 - a1 * x1
        # print(f"a1: {a1}, b1: {b1}")

        if x3 == x4:
            x_int = x3
            y_int = a1 * x_int + b1
            print(f"POINT {x_int:.2f} {y_int:.2f}")

        else:
            a2 = (y4 - y3)/(x4 - x3)
            b2 = y3 - a2 * x3
            # print(f"a2: {a2}, b2: {b2}")


            if a1 == a2:
                if b1 == b2:
                    print("LINE")
                else:
                    print("NONE")
            
            else:
                x_int = (b2 - b1)/(a1 - a2)
                y_int = a1 * x_int + b1
                print(f"POINT {x_int:.2f} {y_int:.2f}")

print("END OF OUTPUT")