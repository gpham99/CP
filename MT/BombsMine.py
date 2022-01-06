from queue import Queue
r_p = [0, 1, 0, -1]
c_p = [1, 0, -1, 0]

def BFS(board, dist, x_s, y_s, x_e, y_e, R, C):
    visited = set()
    q = Queue()
    q.put((x_s, y_s))
    visited.add((x_s, y_s))
    
    while not q.empty():
        x, y = q.get()
        if x == x_e and y == y_e:
            return dist[x][y]

        for z in range(4):
            r = x + r_p[z]
            c = y + c_p[z]
            if r in range(R) and c in range(C) and (r, c) not in visited and board[r][c] != 1:
                q.put((r, c))
                visited.add((r, c))
                dist[r][c] = dist[x][y] + 1

def main():
    R, C = map(int, input().split())
    while not (R == 0 and C == 0):
        n_rows = int(input())
        board = [[0 for i in range(C)] for i in range(R)] # no bomb = 0, bombs = 1
        dist = [[0 for i in range(C)] for i in range(R)]
        for i in range(n_rows):
            line = list(input().split())
            r = int(line[0])
            n_bombs_in_row = int(line[1])
            for j in range(n_bombs_in_row):
                c = int(line[2 + j])
                board[r][c] = 1
        x_s, y_s = map(int, input().split())
        x_e, y_e = map(int, input().split())

        print(BFS(board, dist, x_s, y_s, x_e, y_e, R, C))
        R, C = map(int, input().split()) # input ends

if __name__ == "__main__":
    main()