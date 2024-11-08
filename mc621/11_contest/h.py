t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]

    primeira = input()
    segunda = input()

    set_primeira = {}
    set_segunda = {}

    for letra in primeira:
        set_primeira[letra] = primeira.count(letra)
    
    for letra in segunda:
        set_segunda[letra] = segunda.count(letra)

    sorted(set_primeira.items(), reverse=True)
    sorted(set_segunda.items(), reverse=True)

    i = 0
    did = False

    if len(set_primeira) != len(set_segunda):
        print("No")
        did = True

    # print(set_primeira)
    # print(set_segunda)
    if did == False:
        for prim in list(set_primeira.keys()):
            if set_primeira[prim] != list(set_segunda.values())[i] or (prim > list(set_segunda.keys())[i]):
                print("No")
                did = True
                break
            
            if set_primeira[prim] == 1 and list(set_segunda.values())[i] == 1 and prim != list(set_segunda.keys())[i]:
                print("No")
                did = True
                break
            i += 1
    
    if did == False:
        print("Yes")
    


        
        
