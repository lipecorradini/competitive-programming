def main():

    t = int(input())

    for _ in range(t):
        n = int(input())
        todas = set()
        ordem = []
        ans = ""

        for __ in range(n):
            nova = input()
            todas.add(nova)
            ordem.append(nova)
        
        for i in range(n):
            add = 0
            atual = ordem[i]
            for j in range(len(atual)):
                if atual[:j] in todas and atual[j:] in todas:
                    add = 1
            ans += str(add)
        
        print(ans)

main()