import queue
class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value

def main():
    N = int(input())
    pq = queue.PriorityQueue()
    pq2 = queue.PriorityQueue()
    pivot = 10**9

    for i in range(N):
        operation = list(map(int, input().split()))
        if len(operation) == 2:
            if operation[1] < pivot: # the sign shouldn't matter too much for now -- could be fixed later
                pq.put(PQEntry(operation[1]))
            else:
                pq2.put(operation[1])

        else:
            n_to_get = (len(pq.queue) + len(pq2.queue)) // 3
            if n_to_get == 0:
                print("No reviews yet")
            else:
                if n_to_get == len(pq2.queue):
                    print(pq2.queue[0])
                    # pivot = pq2.queue[0]

                elif n_to_get < len(pq2.queue):
                    index = len(pq2.queue) - n_to_get
                    for i in range(index):
                        pq.put(PQEntry(pq2.get()))

                    pivot = pq2.queue[0]                    
                    print(pivot)

                else:
                    index = n_to_get - len(pq2.queue)
                    for i in range(index - 1):
                        pivot = pq.get().value
                        pq2.put(pivot)
                    print(pq.queue[0].value)
                
if __name__ == "__main__":
    main()