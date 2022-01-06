# bai nay co the xai dict duoc
# vi no unique nen co the xai set duoc luon, nhung ma xai set luc sau nho no xoa 1 value xong bo lai 1 cai y het vao...
    # if you remove it from set, it cost O(N)
# please write up an explanation for this...

import queue

def main():
    Q = int(input())
    pq = queue.PriorityQueue()
    delete = queue.PriorityQueue()
    
    for i in range(Q):
        result = list(map(int, input().split()))
        if len(result) == 1 and result[0] == 3 and not pq.empty():

            while not pq.empty() and not delete.empty() and pq.queue[0] == delete.queue[0]:
                # = function delete
                pq.get()
                delete.get()

            print(pq.queue[0])

        elif len(result) == 2 and result[0] == 1:
            pq.put(result[1])

        elif len(result) == 2 and result[0] == 2:
            delete.put(result[1])    

if __name__ == "__main__":
    main()