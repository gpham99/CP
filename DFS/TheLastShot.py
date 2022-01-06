def DFS(N, graph, i): # i = starting point
    visited = [False for i in range(N + 1)]
    s = []
    max_impact = 0
    
    s.append(i)
    visited[i] = True
    
    while len(s) > 0:
        v = s.pop()
        max_impact += 1

        for neighbor in graph[v]:
            if visited[neighbor] == False:
                s.append(neighbor)
                visited[neighbor] = True

    return max_impact


def main():
    N, M = map(int, input().split()) # bombs, relations
    graph = [[] for i in range(N + 1)]
    max_impact = 0

    # prepare the graph
    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    for i in range(1, N + 1, 1): # each vertex ~ bomb
        if DFS(N, graph, i) > max_impact:
            max_impact = DFS(N, graph, i)

    return max_impact

if __name__ == '__main__':
    print(main())