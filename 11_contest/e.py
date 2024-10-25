

def main():

    p = int(input())
    # prev = 1

    # for i in range(1, p + 1):
    #     prev *= i
    #     facts.add(prev)
    
    # print(facts)

    # # p[i] = fatorial[i]
    # count = 0
    # great = max(facts)
    # for n in range(2, p + 1):
    #     if n in facts and n != great: # pega o fatorial de p - 1
    #         count += 1
    
    # print(count)
    if p == 0 or p == 1:
        print(0)
        return


    print(p - 2)

main()