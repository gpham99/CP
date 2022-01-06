from queue import Queue

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def main():
    check = True
    while check:
        N, M = map(int, input().split()) # rows, columns
        if N == 0 and M == 0:
            check = False
        else:
            board = []
            for i in range(N):
                line = list(input().split())
                board.append(line)

            n_slicks = 0
            visited = set()
            slicks = {}

            q = Queue()
            # find the first cell that has the slick
            for i in range(N):
                for j in range(M):
                    if board[i][j] == '1' and (i, j) not in visited:
                        n_slicks += 1 # subject to fix
                        q.put((i, j))
                        visited.add((i, j))
                        size = findSlicks(q, visited, board, N, M)
                        if size in slicks:
                            slicks[size] += 1
                        else:
                            slicks[size] = 1
            
            print(n_slicks)
            for key in sorted(slicks):
                print(key, slicks[key])


def findSlicks(q, visited, board, N, M):
    size = 0
    while not q.empty():
        x, y = q.get()
        size += 1
        
        for z in range(4):
            r = x + dr[z]
            c = y + dc[z]
            
            if r in range(N) and c in range(M) and (r, c) not in visited and board[r][c] == '1':
                q.put((r, c))
                visited.add((r, c))
    return size

if __name__ == '__main__':
    main()