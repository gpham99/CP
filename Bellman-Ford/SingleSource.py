INF = int(1e9)
class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

def BF(graph, dist, s, n, m):
    dist[s] = 0
    for i in range(n - 1):
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    for i in range(n - 1):
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF

def main():
    n, m, q, s = map(int, input().split())
    while not (n == 0 and m == 0 and q == 0 and s == 0):
        graph = []
        dist = [INF for i in range(n)]
        for i in range(m):
            u, v, w = map(int, input().split())
            graph.append(Edge(u, v, w))
        
        BF(graph, dist, s, n, m)
        
        for _ in range(q):
            d = int(input())
            if dist[d] == INF:
                print("Impossible")
            elif dist[d] == -INF:
                print("-Infinity")
            else:
                print(dist[d])

        n, m, q, s = map(int, input().split()) # read next input
        if not (n == 0 and m == 0 and q == 0 and s == 0):
            print()

if __name__ == "__main__":
    main()