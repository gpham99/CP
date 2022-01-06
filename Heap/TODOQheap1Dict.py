import queue

def main():
    Q = int(input())
    pq = queue.PriorityQueue()
    delete = dict()
    
    for i in range(Q):
        result = list(map(int, input().split()))

        if len(result) == 1 and result[0] == 3 and not pq.empty():
            while not pq.empty() and not delete.empty() and pq.queue[0] == delete.queue[0]:
                # dieu kien no phai lon hon 0, vi neu no hon thi no phai cham dut vong while

                # = function delete
                pq.get()
                delete.get() # -> giam occurence o trong dict

            print(pq.queue[0])

        elif len(result) == 2 and result[0] == 1:
            pq.put(result[1])

        elif len(result) == 2 and result[0] == 2:
            if result[1] in delete:
                delete[result[1]] += 1
            else:
                delete[result[1]] = 1

if __name__ == "__main__":
    main()