from queue import Queue

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def main():
    n_tests = int(input())
    for i in range(n_tests):
        board = []
        w, h = map(int, input().split())
        
        q = Queue()
        count = 1
        visited = [[False for x in range(w)] for y in range(h)]  # wrong approach: [[False] * w] * h

        # save board
        for y in range(h):
            line = list(input().strip())    # strip - not have trailing whitespaces, list - split on individual characters
            board.append(line)

        # find loc of prince
        for j in range(h):
            for k in range(w):
                if board[j][k] == '@':
                    q.put((j, k))
                    visited[j][k] = True

        while not q.empty():
            j, k = q.get() # j = the line it's on, and k = the column

            for z in range(4):
                r = j + dr[z]
                c = k + dc[z]

                if r in range(h) and c in range(w) and visited[r][c] == False and board[r][c] != '#':
                    q.put((r, c))
                    visited[r][c] = True       
                    count += 1             
                
        print("Case {}: {}".format(i + 1, count))                    

main()