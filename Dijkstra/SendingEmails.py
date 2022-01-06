INF = int(1e9)
import queue

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(S, T, graph, dist):
    pq = queue.PriorityQueue()
    pq.put(Node(S, 0))
    dist[S] = 0

    while not pq.empty():
        top = pq.get()
        u = top.id
        if u == T:
            return dist[T]
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, dist[neighbor.id]))
    return dist[T]
    
def main():
    Q = int(input())
    for i in range(Q):
        N, M, S, T = map(int, input().split()) # n = nodes, m = edges
        graph = [[] for _ in range(N)]
        dist = [INF for _ in range(N)]
        for j in range(M):
            a, b, w = map(int, input().split())
            graph[a].append(Node(b, w))
            graph[b].append(Node(a, w))
        # find shortest path
        latency = Dijkstra(S, T, graph, dist)
        if latency == INF:
            print("Case #{}: unreachable".format(i + 1))
        else:
            print("Case #{}: {}".format(i + 1, latency))
            
if __name__ == "__main__":
    main()