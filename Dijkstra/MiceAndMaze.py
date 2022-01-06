import queue
INF = int(1e9)

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(s, time, graph):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    time[s] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < time[neighbor.id]: # bc time[neighbor.id] was first set to INF
                time[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, time[neighbor.id]))

def main():
    N = int(input())    # no cells
    E = int(input())    # id of exit cell
    T = int(input())    # countdown timer
    M = int(input())    # connections in maze
    n_mice = 0
    graph = [[] for i in range(N)]
    time = [INF for i in range(N)]
    for i in range(M):
        a, b, d = map(int, input().split())     # a -> b
        a -= 1
        b -= 1
        graph[b].append(Node(a, d))
    Dijkstra(E - 1, time, graph)
    # go over time and check if it <= T
    for t in time:
        if t <= T:
            n_mice += 1
    print(n_mice)

if __name__ == "__main__":
    main()