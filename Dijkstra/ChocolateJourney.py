import heapq
INF = int(1e9)

def Dijkstra(s, graph, N):
    dist = [INF for i in range(N)]
    h = []
    heapq.heappush(h, (0, s)) # dist, then id
    dist[s] = 0

    while len(h) != 0:
        tuple = heapq.heappop(h)
        u = tuple[1]
        w = tuple[0]
        if dist[u] != w:
            continue
        for neighbor in graph[u]:
            n_u = neighbor[1]
            n_w = neighbor[0]
            if w + n_w < dist[n_u]:
                dist[n_u] = w + n_w
                heapq.heappush(h, (dist[n_u], n_u))
    return dist

def main():
    N, M, k, x = map(int, input().split())
    chocolate_cities = list(map(int, input().split())) # indexed from 1 to N

    graph = [[] for i in range(N)]
    for i in range(M):
        u, v, d = map(int, input().split())
        u -= 1
        v -= 1 
        graph[u].append((d, v))
        graph[v].append((d, u))
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    
    dist_A = Dijkstra(A, graph, N)
    dist_B = Dijkstra(B, graph, N)
    min_time = INF
    
    for city in chocolate_cities:
        city -= 1
        if dist_B[city] <= x and dist_A[city] + dist_B[city] < min_time:
            min_time = dist_A[city] + dist_B[city]
    
    if min_time == INF:
        print(-1)
        return
    print(min_time)

if __name__ == "__main__":
    main()