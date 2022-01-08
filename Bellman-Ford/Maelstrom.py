INF = int(1e9)
class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

def BF(s):
    dist[s] = 0
    for x in range(n - 1):
        for y in range(len(graph)):
            u = graph[y].source
            v = graph[y].target
            w = graph[y].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # what if everything is in a cycle hmmm -> read the prompt again, maybe expense cannot be negative

if __name__ == "__main__":
    n = int(input())
    graph = []
    dist = [INF for i in range(n)]
    for i in range(n - 1):
        line = list(input().split())
        for j in range(i + 1):
            if line[j] != 'x':
                graph.append(Edge(i + 1, j, int(line[j])))
                graph.append(Edge(j, i + 1, int(line[j])))
    BF(0)
    print(max(dist))