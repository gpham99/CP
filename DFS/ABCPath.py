dr = [1, 0, -1, 0, 1, -1, 1, -1]
dc = [0, 1, 0, -1, 1, 1, -1, -1]

def DFS(H, W, board, dist, i, j):
    if dist[i][j] != 0:
        return dist[i][j]
    else:
        local_max = 0
        for z in range(8):
            r = i + dr[z]
            c = j + dc[z]
            if r in range(H) and c in range(W) and ord(board[r][c]) == ord(board[i][j]) + 1:
                # print("r, c, letter: ", r, c, board[r][c])
                # dist[r][c] = max(DFS(H, W, board, dist, r, c), dist[r][c])
                # print("dist: ", dist)
                local_max = max(DFS(H, W, board, dist, r, c), local_max)
        return local_max + 1

def main():
    case = 0
    run = True
    while run:
        H, W = map(int, input().split())
        if H == 0 and W == 0:
            run = False
            break

        case += 1
        board = []
        dist = [[0 for i in range(W)] for i in range(H)]
        max_path = 0

        # prep the board
        for i in range(H):
            line = list(input())
            board.append(line)

        # find As
        for i in range(H):
            for j in range(W):
                if board[i][j] == 'A':
                    max_path = max( DFS(H, W, board, dist, i, j) , max_path)
        print("Case {}:".format(case), max_path)

if __name__ == "__main__":
    main()