inf = 1e10 + 1

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def main():
    t = int(input())

    for _ in range(t):
        n, k, a, b = [int(x) for x in input().split()]
        cities = []
        k -= 1
        a -= 1
        b -= 1
        for __ in range(n):
            x, y = [int(x) for x in input().split()]
            cities.append([x, y])
        
        if a <= k and b <= k:
            print(0)

        elif a <= k: # a ou b major
            min_dist = inf
            for i in range(k + 1):
                if distance(cities[b], cities[i]) < min_dist:
                    min_dist = distance(cities[b], cities[i])
            print(min_dist)
        
        elif b <= k: # a ou b major
            min_dist = inf
            for i in range(k + 1):
                if distance(cities[a], cities[i]) < min_dist:
                    min_dist = distance(cities[a], cities[i])
            print(min_dist)
        
        else:
            min_dist_a = inf
            min_dist_b = inf

            for i in range(k + 1):
                if distance(cities[a], cities[i]) < min_dist_a:
                    min_dist_a = distance(cities[a], cities[i])

                if distance(cities[b], cities[i]) < min_dist_b:
                    min_dist_b = distance(cities[b], cities[i])
            
            dist_a_b = distance(cities[a], cities[b])

            print(min(dist_a_b, min_dist_a + min_dist_b))
            
main()
