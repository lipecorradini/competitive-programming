import bisect

n, q = [int(x) for x in input().split()]

graph = {}
for i in range(1, n + 1):
    graph[i] = [i]

for i in range(q):
    type, u, v = [int(x) for x in input().split()]
    if type == 1:
        
        if (graph[u][0] > 0):
            graph[u] = list(set(graph[u] + graph[v]))
            graph[v] = [-u]
            # bisect.insort(graph[u], v)

        if graph[v][0] > 0 and graph[u][0] < 0:
            graph[v] = list(set(graph[u] + graph[v]))
            graph[u] = [-v]

        

            

        

    
    if type == 2:
        print(f"u: {u}, v: {v}")
        print(f"adj[{u}] = ", graph[u])
        if len(graph[u]) < v:
            print(-1)
        else:
            print(graph[u][-v])
    

