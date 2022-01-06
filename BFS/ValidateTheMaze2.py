import queue

def BFS(visited, path, graph, s):
    q = queue.Queue()
    visited[s] = True
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u  

def isPath(visited, path, graph, s, f):
    while True:
        f = path[f]
        if f == s:
            return True
        elif f == -1:
            break
    return False

def singleMazeTest():
    M, N = map(int, input().split()) # rows, columns

    # read all the lines of input and transcribe it into a board
    board = []
    for i in range(M):
        line = list(input().rstrip())
        board.append(line)

    visited = [False for i in range(M * N)]
    path = [-1 for i in range(M * N)]
    graph = [[] for i in range(M * N)]
    
    # each character is a vertex on the graph
        # graph[index of that character].append(v)
        # what should v be?
        # v should be the index of the other character that it's connected to...

    # how to eval the entries? you can still read through the four edges of the board
    # put their index onto the entries_set
    # otherwise, eliminate
    # you can merge this onto the part above
    entries_set = set()
    M_val = M
    # read through the board and create the graph
    for i in range(M): # row
        for j in range(N): # column
            if board[i][j] == '.':
                if i < M - 1 and board[i + 1][j] == '.':
                    if N == 1:
                        M_val = 1
                    # print("before it dies: ", i, j)
                    graph[M_val * i + j].append(M_val * (i + 1) + j) # one way
                    # print("after it dies: ", i, j)
                    graph[M_val * (i + 1) + j].append(M_val * i + j) # the other way
                if j < N - 1 and board[i][j + 1] == '.':
                    graph[M_val * i + j].append(M_val * i + (j + 1)) # one way
                    graph[M_val * i + (j + 1)].append(M_val * i + j) # the other way

                if i == 0 or i == M - 1 or j == 0 or j == N - 1:
                    entries_set.add(M_val * i + j)
    # print(graph)
    # print(entries_set)

    if len(entries_set) != 2:
        return False

    s = entries_set.pop()
    f = entries_set.pop()
    BFS(visited, path, graph, s)
    return isPath(visited, path, graph, s, f)

def validateTheMaze():
    T = int(input())
    for i in range(T):
        if singleMazeTest():
            print("valid")
        else:
            print("invalid")

validateTheMaze()