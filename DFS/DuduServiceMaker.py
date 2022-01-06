import sys
sys.setrecursionlimit(10**9)

def DFS(onPath, graph, s, visited):
    visited[s] = True
    onPath[s] = True

    for v in graph[s]: # base case
        if onPath[v]:
            return True
        if visited[v] == False: # recursive case
            if DFS(onPath, graph, v, visited):
                return True
    onPath[s] = False

def eachTest():
    N, M = map(int, input().split()) # docs, dependencies
    graph = [[] for i in range(N + 1)]
    onPath = [False for i in range(N + 1)]
    visited = [False for i in range(N + 1)]

    for j in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    for z in range(N):
        if DFS(onPath, graph, z + 1, visited):
            return "YES"
    return "NO"

def main():
    T = int(input())
    for i in range(T):
        print(eachTest())

if __name__ == '__main__':
    main()