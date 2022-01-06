# tim index trong mang bien no thanh O(N)

def minHeapifyDown(h, i):
    smallest = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left < len(h) and h[left] < h[smallest]:
        smallest = left
    if right < len(h) and h[right] < h[smallest]:
        smallest = right
    if smallest != i:
        h[i], h[smallest] = h[smallest], h[i]
        minHeapifyDown(h, smallest)

def minHeapifyUp(h, i):
    bool = False
    while i != 0 and h[(i - 1) // 2] > h[i]:
        bool = True
        h[i], h[(i - 1) // 2] = h[(i - 1) // 2], h[i]
        i = (i - 1) // 2
    return bool

def push(h, value):
    h.append(value)
    i = len(h) - 1
    minHeapifyUp(h, i)

def pop(h, value):
    length = len(h)
    if length == 0:
        return
    i = h.index(value)
    h[i] = h[length - 1]
    h.pop()
    if i == length - 1:
        return
    bool = minHeapifyUp(h, i)
    if not bool:
        minHeapifyDown(h, i)

def top(h):
    return h[0]
    
def main():
    Q = int(input())
    h = []
    for i in range(Q):
        result = list(map(int, input().split()))
        if len(result) == 1 and result[0] == 3 and len(h) > 0:
            print(top(h))
        elif len(result) == 2 and result[0] == 1:
            push(h, result[1])
        elif len(result) == 2 and result[0] == 2:
            pop(h, result[1])

if __name__ == "__main__":
    main()