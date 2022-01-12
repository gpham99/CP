INF = int(1e9)

def WF(M):
    for k in range(M):
        for i in range(M):
            if matrix[i][k] == INF: # no way from i to k
                continue
            for j in range(M):
                if matrix[k][j] != INF:
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        matrix = []
        line = list(input())
        matrix.append(line)
        M = len(line)

        for j in range(M - 1):
            matrix.append(list(input()))
        
        for a in range(M):
            for b in range(M):
                if matrix[a][b] == 'Y':
                    matrix[a][b] = 1
                else:
                    if a == b:
                        matrix[a][b] = 0
                    else:
                        matrix[a][b] = INF
        WF(M)

        w_friends = 0
        w = 0
        for z in range(M): # z corresponds to id
            p_friends = matrix[z].count(2)

            if p_friends > w_friends:
                w_friends = p_friends
                w = z

        print(w, w_friends)