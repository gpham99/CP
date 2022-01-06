from queue import Queue

def main():
    s_key, l_key = map(int, input().split())
    n_skeys = int(input())
    lst_skeys = list(map(int, input().split()))

    dist = [-1 for i in range(l_key + 1)]
    q = Queue()
    q.put(s_key)
    dist[s_key] += 1 # = 0

    while not q.empty():
        u = q.get()
        for i in range(n_skeys):
            v = (u * lst_skeys[i]) % 100000
            if v == l_key:
                dist[l_key] = dist[u] + 1
                print(dist[l_key])
                return
            if v < l_key and dist[v] == -1:
                q.put(v)
                dist[v] = dist[u] + 1
            
    print(dist[l_key])
    return

main()