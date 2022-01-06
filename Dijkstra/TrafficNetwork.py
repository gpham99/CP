INF = int(1e9)
import heapq

def Dijkstra(s, graph, N):
    dist = [INF for i in range(N)]
    h = []
    dist[s] = 0
    heapq.heappush(h, (0, s))
    while len(h) != 0:
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
    d = int(input())
    for i in range(d):
        N, M, K, S, T = map(int, input().split())
        graph_for_S = [[] for _ in range(N)]
        graph_for_T = [[] for _ in range(N)] # reverse direction

        for j in range(M):
            d, c, l = map(int, input().split())
            d -= 1
            c -= 1
            graph_for_S[d].append((l, c)) # dist, id
            graph_for_T[c].append((l, d))

        dist_S = Dijkstra(S - 1, graph_for_S, N)
        dist_T = Dijkstra(T - 1, graph_for_T, N)
        current_shortest = dist_S[T - 1]
        
        for k in range(K):
            u, v, q = map(int, input().split())
            u -= 1
            v -= 1
            if dist_S[u] + dist_T[v] + q < current_shortest or dist_S[v] + dist_T[u] + q < current_shortest:
                current_shortest = min(dist_S[u] + dist_T[v] + q, dist_S[v] + dist_T[u] + q)

        if current_shortest == INF:
            print(-1)
        else:
            print(current_shortest)

if __name__ == "__main__":
    main()