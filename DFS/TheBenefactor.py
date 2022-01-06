from sys import stdin

def DFS(visited, grid, v):
    visited.add(v)
    local_m_l = 0
    true_node = v
    for i in range(len(grid[v])): # index repping vertex
        if grid[v][i] != 0 and i not in visited: # != 0 meaning neighbor
            length, node = DFS(visited, grid, i)
            # local_m_l = max( local_m_l, length + grid[v][i] )
            if length + grid[v][i] > local_m_l:
                local_m_l = length + grid[v][i]
                true_node = node

    return local_m_l, true_node

def main():
    t = int(input())
    for test in range(t):
        n_places = int(input())
        grid = [[0 for i in range(n_places)] for i in range(n_places)]
        
        for i in range(n_places - 1):
            line = input()
            x, y, z = map(int, line.split())
            x, y = x - 1, y - 1
            grid[x][y] = z
            grid[y][x] = z
        
        node = 0
        for v in range(2): # ~ vertex
            visited = set()
            max_length, node = DFS(visited, grid, node)
        print(max_length)

if __name__ == "__main__":
    main()