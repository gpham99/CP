from sys import stdin

def DFS(i, graph, n_places): # i la diem bat dau
    s = []
    visited = set()
    dist = [0 for i in range(n_places)]

    s.append(i)
    visited.add(i)
    max_length = 0
    leaf = 0
    
    while len(s) > 0:
        i = s.pop()
        
        for neighbor in graph[i]:
            x = neighbor[0]
            weight = neighbor[1]

            if x not in visited:
                dist[x] = dist[i] + weight
                s.append(x)
                visited.add(x)
                if dist[x] > max_length:
                    max_length = dist[x]
                    leaf = x
    return max_length, leaf

def main():
    t = int(input())
    for test in range(t):
        n_places = int(input())
        graph = [[] for i in range(n_places)]

        for i in range(n_places - 1):
            line = input()
            x, y, z = map(int, line.split())
            x, y = x - 1, y - 1
            graph[x].append((y,z))
            graph[y].append((x,z))

        # run DFS from a vertex -> return the greatest length AND the vertex on the other side of greatest length
        # chon dinh bat dau la vertex 0
        
        length1, node_1 = DFS(0, graph, n_places)
        length2, node_2 = DFS(node_1, graph, n_places)
        print(length2)

if __name__ == "__main__":
    main()