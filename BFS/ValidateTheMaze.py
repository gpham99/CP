# once you found those 2 pts, you start doing the path search
# each test case

import queue
def BFS(graph, path, visited, s):
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

def isPath(graph, path, visited, s, f):
    while True:
        f = path[f]
        if f == s:
            return True
        elif f == -1:
            break
    return False

def eachTest():
    M, N = map(int, input().split()) # rows, columns
    # init a list of pt
    pt_lst = []
    # check for valid entries - entries holding the index of the pt!
    entries = set()

    # read the maze
    for i in range(M):
        line = list(input().strip())
        for j in range(N):
            if line[j] == '.':
                pt_lst.append((i, j))
    # print(pt_lst)

    MAX = len(pt_lst) # denotes the no of vertices
    for i in range(MAX):
        if pt_lst[i][0] == 0 or pt_lst[i][0] == M - 1 or pt_lst[i][1] == 0 or pt_lst[i][1] == N - 1:
            entries.add(i)
    # print("entries: ", entries)

    if len(entries) != 2:
        print("invalid")
        return

    visited = [False for i in range(MAX)]
    path = [-1 for i in range(MAX)]
    graph = [[] for i in range(MAX)]

    # starting the BFS thing
    #   set up the graph using the list
    for u in range(MAX):
        for v in range(MAX):
            if pt_lst[u] == (pt_lst[v][0] - 1, pt_lst[v][1]) or pt_lst[u] == (pt_lst[v][0] + 1, pt_lst[v][1]) or pt_lst[u] == (pt_lst[v][0], pt_lst[v][1] + 1) or pt_lst[u] == (pt_lst[v][0], pt_lst[v][1] - 1):
                graph[u].append(v)
    # print("graph: ", graph)

    # how to get the entries
    # how to get the graph 

    s = entries.pop()
    f = entries.pop()

    BFS(graph, path, visited, s)
    # print(path)

    if isPath(graph, path, visited, s, f):
        print("valid")
        return
    else:
        print("invalid")
        return

def isValidMaze():
    T = int(input())
    for i in range(T):
        eachTest()

isValidMaze()