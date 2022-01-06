import sys
sys.setrecursionlimit(10**9)

dr = [0, 1, -1, 0, 1, -1, 1, -1]
dc = [1, 0, 0, -1, 1, 1, -1, -1]
sentence = "ALLIZZWELL"

def DFS(R, C, count, sentence, board, visited, i, j): # a cell that contains A
    if count == len(sentence): # base case
        return True
    visited[i][j] = True

    for z in range(8):
        r = i + dr[z]
        c = j + dc[z]

        # print("r c: ", r, c)
        if r in range(R) and c in range(C) and board[r][c] == sentence[count] and not visited[r][c]:
            # print(r, c, board[r][c])
            if DFS(R, C, count + 1, sentence, board, visited, r, c): # if statement to pass it back
                return True
            visited[r][c] = False
    return False

def eachTest():
    R, C = map(int, input().split())
    visited = [[False for i in range(C)] for i in range(R)]
    board = []
    
    # prep board
    for i in range(R):
        line = list(input())
        board.append(line)

    # find the 'first' location of A
    for i in range(R):
        for j in range(C):
            if board[i][j] == sentence[0]:
                if DFS(R, C, 1, sentence, board, visited, i, j) == True:
                    return "YES"
                visited[i][j] = False
    return "NO"

def main():
    t = int(input()) # n_tests
    for i in range(t):
        print(eachTest())
        input()

if __name__ == "__main__":
    main()