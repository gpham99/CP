import queue

class Car:
    def __init__(self, id, arr_time):
        self.id = id
        self.arr_time = arr_time

def main():
    C = int(input())
    for z in range(C):
        N, T, M = map(int, input().split()) # capactiy, time to cross, lines to follow        
        left = queue.Queue()
        right = queue.Queue()
        for j in range(M):
            line = list(input().split())
            arr_time = int(line[0])
            side = str(line[1])
            if side == 'left':
                left.put(Car(j, arr_time))
            else:
                right.put(Car(j, arr_time))

        # simulate
        unload_arr = [0 for _ in range(M)]
        curr_time = 0
        curr_side = 1 # left = 1, right = 0

        while not (left.empty() and right.empty()):
            if not left.empty() and right.empty():
                next_time = left.queue[0].arr_time
            elif  not right.empty() and left.empty():
                next_time = right.queue[0].arr_time
            else:
                next_time = min(left.queue[0].arr_time, right.queue[0].arr_time)
            
            if curr_time < next_time:
                curr_time = next_time

            if curr_side == 1: # left
                i = 0             
                while not left.empty() and curr_time >= left.queue[0].arr_time and i < N:
                    car = left.get()
                    unload_arr[car.id] = curr_time + T
                    i += 1
            else: # right
                i = 0             
                while not right.empty() and curr_time >= right.queue[0].arr_time and i < N:
                    car = right.get()
                    unload_arr[car.id] = curr_time + T
                    i += 1
            curr_side = 1 - curr_side
            curr_time += T


            # curr_time >= first element -> pop that off, move curr_side to the other side, append the necessary
            # time to unload_arr
            
            # if not
            # -> move to the other side
            # -> update curr_time

        for unload_t in unload_arr:
            print(unload_t)
        if z != C - 1:
            print()

if __name__ == "__main__":
    main()