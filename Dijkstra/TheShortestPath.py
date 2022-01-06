import queue
INF = 200000

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(s, e, graph, n):
    dist = [INF for i in range(n)]
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    
    while not pq.empty():
        top = pq.get()
        u = top.id
        if u == e:
            return dist[e]
        w = top.dist
        for neighbor in graph[u]:
            if neighbor.dist + w < dist[neighbor.id]:
                dist[neighbor.id] = neighbor.dist + w
                pq.put(Node(neighbor.id, dist[neighbor.id]))
    return dist[e]

def main():
    s = int(input())    # n of tests
    for i in range(s):
        n = int(input())    # n of cities
        graph = [[] for _ in range(n)]
        c_name_dict = dict()
        
        for j in range(n):
            c_name = input()
            c_name_dict[c_name] = j
            c_neighbors = int(input())

            for k in range(c_neighbors):
                n_id, d = map(int, input().split())
                n_id -= 1
                graph[j].append(Node(n_id, d))

        # fin. graph
        # print(c_name_dict)
        r = int(input())
        for i in range(r):
            name_1, name_2 = map(str, input().split())
            print(Dijkstra(c_name_dict[name_1], c_name_dict[name_2], graph, n))
        input() # empty line at the end

if __name__ == "__main__":
    main()