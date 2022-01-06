import heapq 
INF = int(1e9)

def Dijkstra(graph, s, N):
    dist = [INF for i in range(N)]
    h = []
    dist[s] = 0
    heapq.heappush(h, (0, s)) # dist, id
    while h:
        w, u = heapq.heappop(h)
        if dist[u] != w:
            continue
        for neighbor in graph[u]:
            n_w = neighbor[0]
            n_u = neighbor[1]
            if w + n_w < dist[n_u]:
                dist[n_u] = w + n_w
                heapq.heappush(h, (dist[n_u], n_u))
    return dist

def main():
    T = int(input())
    for i in range(T):
        N = int(input()) # n_nodes
        R = int(input()) # n_roads
        graph = [[] for _ in range(N)]
        for j in range(R):
            u, v = map(int, input().split())
            graph[u].append((1, v)) # dist, id
            graph[v].append((1, u))
        s, d = map(int, input().split())
        dist_s = Dijkstra(graph, s, N)
        dist_d = Dijkstra(graph, d, N)
        
        complete_time = -1
        
        for z in range(N):
            if dist_s[z] + dist_d[z] > complete_time:
                complete_time = dist_s[z] + dist_d[z]
                
        print("Case {}: {}".format(i + 1, complete_time))

if __name__ == "__main__":
    main()