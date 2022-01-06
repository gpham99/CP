from queue import Queue

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def BFS(board, n, m, r1,c1,r2,c2):
    q = Queue()
    q.put((r1, c1))

    while not q.empty():
        u1, v1 = q.get()

        # check the 4 slots surrounding that slot
        for i in range(4):
            r_index = u1 + dr[i]
            c_index = v1 + dc[i]

            # problem section
            if r_index == r2 and c_index == c2 and board[r_index][c_index] == 'X':
                return True

            if r_index in range(n) and c_index in range(m) and board[r_index][c_index] == '.':
                board[r_index][c_index] = 'X'
                q.put((r_index, c_index))
            # end of problem section
    return False

def main():
    n, m = map(int, input().split()) # nrows, ncols
    board = []
    for i in range(n):
        line = list(input())
        board.append(line)
    # print(board)
    r1, c1 = map(int, input().split()) # init coord
    r1, c1 = r1-1,c1-1 # so that we can access board 

    r2, c2 = map(int, input().split()) # ending coord
    r2,c2 = r2-1, c2-1 # so that we can access board

    print("YES" if BFS(board, n, m, r1,c1,r2,c2) else "NO")

main()