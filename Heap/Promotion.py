# dung set cung khong duoc, phai dung dict moi duoc vi phai dem so lan no ton tai va bi xoa ra

import queue
class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value

def main():
    n = int(input())
    prizes = 0
    max_pq = queue.PriorityQueue()
    min_pq = queue.PriorityQueue()
    visited = dict()

    for i in range(n):
        day = list(map(int, input().split()))
        n_receipts = day[0]
        for z in range(1, n_receipts + 1, 1):
            r = day[z]
            min_pq.put(r)
            max_pq.put(PQEntry(r))

            if r in visited:
                visited[r] += 1
            else:
                visited[r] = 1
        
        # the end of the day
        while visited[max_pq.queue[0].value] == 0: # this means it should already be gone
            max_pq.get()
        if not max_pq.empty():
            daily_max = max_pq.get().value
            visited[daily_max] -= 1
        else:
            daily_max = 0

        while visited[min_pq.queue[0]] == 0:
            min_pq.get()
        if not min_pq.empty():
            daily_min = min_pq.get()
            visited[daily_min] -= 1
        else:
            daily_min = 0

        prizes += daily_max - daily_min

        # after we do this, the min is still in the max and the max is still in the min
        # we need to decrement them in the dictionary -> for what?
            # when we get something and the count inside the dict is 0 -> get the next one
        # do you need to remove anything from the dictionary though?
        
    print(prizes)

if __name__ == "__main__":
    main()