INF = int(1e9)
class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

def BF(s):
    dist[s] = 0
    for i in range(N - 1):
        for j in range(M):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if dist[u] != -INF and dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
    
    for j in range(M):
        u = graph[j].source
        v = graph[j].target
        w = graph[j].weight
        if dist[u] != -INF and dist[u] + w > dist[v]:
            return True
    return False

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, M = map(int, input().split())
        graph = []
        dist = [-INF for i in range(N)]
        for j in range(M):
            i, j, C = map(int, input().split())
            graph.append(Edge(i - 1, j - 1, C))
        if BF(0):
            print("Yes")
        else:
            print("No")