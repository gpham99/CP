from sys import stdin

import queue
class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value

def main(): 
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        pq = queue.PriorityQueue()
        s = []
        q = queue.Queue()
        type = [True, True, True] # pq, s, q

        for i in range(n):
            x, y = map(int, input().split())
            if x == 1:
                s.append(y)
                q.put(y)
                pq.put(PQEntry(y))
            elif x == 2:
                if len(s) > 0:
                    s_val = s.pop()
                else:
                    s_val = -1.5

                if not q.empty():
                    q_val = q.get()
                else:
                    q_val = -1.5

                if not pq.empty():
                    pq_val = pq.get().value
                else:
                    pq_val = -1.5

                type[0] = (y == pq_val) and type[0]
                type[1] = (y == s_val) and type[1]
                type[2] = (y == q_val) and type[2]
        
        # print type
        if sum(type) == 0:
            print("impossible")
        elif sum(type) > 1:
            print("not sure")
        elif type[0] == 1:
            print("priority queue")
        elif type[1] == 1:
            print("stack")
        else:
            print("queue")

if __name__ == "__main__":
    main()