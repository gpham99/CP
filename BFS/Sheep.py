from queue import Queue
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def BFS(N, M, board, q, visited):
    local_sheep = 0
    local_wolf = 0
    edge = False

    while not q.empty():
        i, j = q.get()

        if i in [0, N - 1] or j in [0, M - 1]:
            edge = True

        if board[i][j] == 'k':
            local_sheep += 1
        elif board[i][j] == 'v':
            local_wolf += 1

        for z in range(4):
            r = i + dr[z]
            c = j + dc[z]

            if r in range(N) and c in range(M) and (r, c) not in visited and board[r][c] != '#':
                q.put((r, c))
                visited.add((r, c))
    
    if edge:
        return local_sheep, local_wolf
    else:
        if local_sheep > local_wolf:
            return local_sheep, 0
        else:
            return 0, local_wolf

def main():
    N, M = map(int, input().split()) # r, c
    board = []
    
    for i in range(N):
        line = list(input())
        board.append(line)
    
    q = Queue()
    visited = set()
    sheep = 0
    wolf = 0

    for i in range (N):
        for j in range(M):
            # find all the valid dots
            if board[i][j] != '#' and (i, j) not in visited:
                q.put((i, j))
                visited.add((i, j))
                local_sheep, local_wolf = BFS(N, M, board, q, visited) # change the nums of sheep and wolf
                sheep += local_sheep
                wolf += local_wolf
            
    print(sheep, wolf)

if __name__ == '__main__':
    main()