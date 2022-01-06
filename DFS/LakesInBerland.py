dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def DFS(n, m, board, s, visited):
    size_of_lake = []
    is_edge = False

    while len(s) > 0:
        i, j = s.pop()
        size_of_lake.append((i, j))
        if i in [0, n - 1] or j in [0, m - 1]:
            is_edge = True

        for z in range(4):
            r = i + dr[z]
            c = j + dc[z]
            if r in range(n) and c in range(m) and (r, c) not in visited and board[r][c] == '.':
                s.append((r, c))
                visited.add((r, c))
    
    if is_edge:
        return 0
    else:    
        return size_of_lake       

def main():
    n, m, k =  map(int, input().split())   # r, c, n_lakes
    board = []
    for i in range(n):
        line = list(input())
        board.append(line)
    
    s = []
    visited = set()
    lakes = [] # mang to chua tat ca mang nho

    for i in range(n):
        for j in range(m):
            if board[i][j] == '.' and (i, j) not in visited: # i not in [0, n - 1] and j not in [0, m - 1] and
                s.append((i, j))
                visited.add((i, j))
                size_of_lake = DFS(n, m, board, s, visited)
                if size_of_lake != 0:
                    lakes.append(size_of_lake)
    # sorted -> mang moi
    # .sort -> tren mang cu

    lakes.sort(key=lambda x: len(x))
    arbitrage = len(lakes) - k
    count = 0

    for y in range(arbitrage):
        lake = lakes[y]
        count += len(lake)
        for x, y in lake:
            board[x][y] = '*'
        
    print(count)
    for i in range(n):
        print("".join(board[i]))
    
    # an array containing the size of each lake
    # the length of that array will be the number of lakes
    # to get to the number of desired lakes -> sort that array and add the first one corresponding
    # to: n_real_lakes - n_required_lakes -> dung for loop or something
    
if __name__ == '__main__':
    main()