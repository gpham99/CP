from queue import Queue

def BFS(s, M, graph, visited, vertexCats, hasCat):
    count = 0
    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()
        if vertexCats[u] <= M:
            for v in graph[u]:
                if hasCat[v] == 0:
                    vertexCats[v] = 0
                else:
                    vertexCats[v] = vertexCats[u] + 1
                
                # consider if v is leaf node
                if len(graph[v]) == 1 and vertexCats[v] <= M:
                    count += 1

                if not visited[v]:
                    visited[v] = True
                    q.put(v)
    return count

def main():
    N, M = map(int, input().split())
    hasCat = list(map(int, input().split()))

    graph = [[] for i in range(N)] # N = no vertices, M = tolerance = max no of conse cats
    for i in range(N - 1):
        x, y = map(int, input().split())
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)
    # print(graph)
    
    visited = [False for i in range(N)]
    vertexCats = [0 for i in range(N)]

    vertexCats[0] = hasCat[0] # may need to think about this again

    s = 0

    # our vertex is automatically 0
    print(BFS(s, M, graph, visited, vertexCats, hasCat)) # print the count

main()