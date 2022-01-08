INF = int(1e9)
class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

def BF(s, graph, dist, n, m): # dist la prob success -> tim max dist
    dist[s] = 1
    for i in range(n - 1):
        for j in range(m * 2):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if (dist[u] != -INF) and (dist[u] * w > dist[v]):
                dist[v] = dist[u] * w

def main():
    line = list(map(int, input().split()))
    while len(line) != 1:
        n, m = line[0], line[1]
        graph = []
        dist = [-INF for i in range(n)]
        for i in range(m):
            a, b, p = map(int, input().split())
            graph.append(Edge(a - 1, b - 1, p / 100))
            graph.append(Edge(b - 1, a - 1, p / 100))
        BF(0, graph, dist, n, m)
        print("{:.6f} percent".format(dist[n - 1] * 100))

        line = list(map(int, input().split()))

if __name__ == "__main__":
    main()