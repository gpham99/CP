from sys import stdin

def DFS(visited, graph, v):
    visited.add(v)
    local_m_l = 0
    true_node = v

    for i, w in graph[v]: 
        if i not in visited:
            length, node = DFS(visited, graph, i)

            if length + w > local_m_l:
                local_m_l = length + w
                true_node = node

    return local_m_l, true_node

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
        
        node = 0
        for v in range(2): # ~ vertex
            visited = set()
            max_length, node = DFS(visited, graph, node)
        print(max_length)

if __name__ == "__main__":
    main()