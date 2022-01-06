INF = int(1e9)
import heapq

def Dijkstra(graph, s, N):
    dist = [INF for i in range(N)]
    h = []
    heapq.heappush(h, (0, s)) # dist, id
    dist[s] = 0

    while h:
        w, u = heapq.heappop(h)
        if dist[u] != w:
            continue
        for neighbor in graph[u]:
            n_w = neighbor[0]
            n_u = neighbor[1]
            if n_w + w < dist[n_u]:
                dist[n_u] = n_w + w
                heapq.heappush(h, (dist[n_u], n_u))
    return dist
    
def main():
    N, M = map(int, input().split()) # nodes, paths
    while not (N == 0 and M == 0):
        S, D = map(int, input().split())
        graph = [[] for i in range(N)]
        r_graph = [[] for i in range(N)]
        reduced_graph = [[] for i in range(N)]
        edges = []
        
        for i in range(M):
            U, V, P = map(int, input().split())
            graph[U].append((P, V)) # dist; id of dest
            r_graph[V].append((P, U))
            edges.append((U, V, P))

        # finished graph
        dist_S = Dijkstra(graph, S, N) # from S to all nodes
        dist_D = Dijkstra(r_graph, D, N) # from D to all nodes
        shortest_path = dist_S[D]
        
        # go over edges to form a new graph
        f_graph = [[] for i in range(N)]
        for z in range(M):
            U, V, P = edges[z]
            if dist_S[U] + dist_D[V] + P != shortest_path:
                f_graph[U].append((P, V))
        
        f_dist = Dijkstra(f_graph, S, N)
        if f_dist[D] == INF:
            print(-1)
        else:
            print(f_dist[D])

        N, M = map(int, input().split()) # next input 

if __name__ == "__main__":
    main()