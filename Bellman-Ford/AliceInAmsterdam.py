INF = 2**30 * 100 # gotta be bigger than when they add altogether later

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

def BF(s):
    dist = [INF for _ in range(N)]
    if self_start_dist[s] < 0:
        dist[s] = self_start_dist[s]
    else:
        dist[s] = 0
    for a in range(N - 1):
        for b in range(len(graph)):
            u = graph[b].source
            v = graph[b].target
            w = graph[b].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for a in range(N - 1):
        for b in range(len(graph)):
            u = graph[b].source
            v = graph[b].target
            w = graph[b].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
    return dist

if __name__ == "__main__":
    N = int(input())
    count = 0
    while N != 0:
        count += 1
        d = dict()
        graph = []
        self_start_dist = [0 for _ in range(N)]
        dist_d = dict()

        for i in range(N):
            line = list(input().split())
            c_name = line[0]
            d[i] = c_name

            for j in range(N):
                if i == j:
                    self_start_dist[i] = int(line[1 + j])
                if int(line[1 + j]) != 0:
                    graph.append(Edge(i, j, int(line[1 + j])))
        
        # for element in graph:
        #     print(element.source, element.target, element.weight)
        
        print("Case #{}:".format(count))
        Q = int(input())
        for k in range(Q):
            s, e = map(int, input().split())
            if s not in dist_d:
                dist_d[s] = BF(s)

            if dist_d[s][e] == -INF:
                print("NEGATIVE CYCLE")
            elif dist_d[s][e] == INF:
                print("{}-{} NOT REACHABLE".format(d[s], d[e]))
            else:
                print("{}-{} {}".format(d[s], d[e], dist_d[s][e]))

        N = int(input())