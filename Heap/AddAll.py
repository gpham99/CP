# khong the xai mang vi moi lan co so moi thi phai cho vao lai va sap xep lai
# cost bi cong lap o trong do

import queue

def main():
    run = True
    while run:
        N = int(input())
        if N == 0:
            run = False
            break
        
        num_lst = list(map(int, input().split()))
        pq = queue.PriorityQueue()
        cost = 0

        for num in num_lst:
            pq.put(num)

        while pq.qsize() > 1: # phai de len > 1 de lay dc 2
            s = 0
            for i in range(2):
                s += pq.get()
            cost += s
            pq.put(s)

        print(cost)
            
if __name__ == '__main__':
    main()