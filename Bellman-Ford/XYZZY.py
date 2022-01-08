from queue import Queue
INF = int(1e9)
class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

def hasPath(s):
    # # consider if there's a path from s to n - 1 -> return True / False
    visited = [False for _ in range(n)]
    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        v = q.get()
        if v == n - 1:
            return True
        for neighbor in bfs_graph[v]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                q.put(neighbor)
    return False

def BF(s):
    # find the max path from s to all the other edges
    dist[s] = 100
    for i in range(n - 1):
        for z in range(n_edges):
            u = graph[z].source
            v = graph[z].target
            w = graph[z].weight
            # print("each edge consideration: ", u, v, w)
            if dist[u] > 0 and dist[u] + w > dist[v]:
                # print("dist[u], dist[v], w: ", dist[u], dist[v], w)
                dist[v] = dist[u] + w
        # print("iteration: ", dist)
    
    # find the positive weight cycles
    for z in range(n_edges):
        u = graph[z].source
        v = graph[z].target
        w = graph[z].weight
        if dist[u] > 0 and dist[u] + w > dist[v] and hasPath(v):
            return True

    if dist[n - 1] > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input())
    while n != -1:
        n_edges = 0
        room_energy_values = [0 for i in range(n)]
        board = []
        graph = []
        dist = [-INF for i in range(n)]
        bfs_graph = [[] for i in range(n)]

        # set up board and room_energy_values
        for i in range(n):
            line = list(map(int,input().split()))
            room_energy_values[i] = line[0]
            r_exits = line[1]
            n_edges += r_exits
            for j in range(r_exits):
                board.append((i, line[2 + j] - 1))
                bfs_graph[i].append(line[2 + j] - 1)

        # go over board and turn it into a graph
        for element in board:
            n_1 = element[0]
            n_2 = element[1]
            graph.append(Edge(n_1, n_2, room_energy_values[n_2]))
        
        # for element in graph:
        #     print("hehe: ", element.source, element.target, element.weight)
        
        BF(0)

        if BF(0):
            print("winnable")
        else:
            print("hopeless")
        
        n = int(input())