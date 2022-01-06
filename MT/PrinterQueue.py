import queue

class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value

def main():
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        line = list(map(int, input().split()))

        pq = queue.PriorityQueue()
        q = queue.Queue()
        time = 0

        for j in range(n):
            pq.put(PQEntry(line[j]))
            q.put((j, line[j]))

        while q:            
            if q.queue[0][1] == pq.queue[0].value:
                time += 1
                id, p_v = q.get()
                pq.get()
                if id == m:
                    break
            else:
                q.put(q.get())
        print(time)

if __name__ == "__main__":
    main()