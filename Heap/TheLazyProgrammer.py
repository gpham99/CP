import queue

class PQEntry:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __lt__(self, other):
        return self.a > other.a # dinh nghia nho hon theo minh

class Contract:
    def __init__(self, a, b, d):
        self.a = a
        self.b = b
        self.d = d
    def __lt__(self, other):
        return self.d < other.d

def main():
    t = int(input())
    for i in range(t):
        S = 0
        pq = queue.PriorityQueue()
        time_spent = 0
        contracts = []

        N = int(input())
        for i in range(N):
            a, b, d = map(int, input().split())
            contracts.append(Contract(a, b, d))
        contracts.sort()

        for contract in contracts:
            time_spent += contract.b

            pq.put(PQEntry(contract.a, contract.b))

            while time_spent > contract.d:
                extra_time = time_spent - contract.d

                top = pq.get()
                a = top.a
                b = top.b

                if b > extra_time:
                    # optimize 1 phan
                    S += extra_time / a
                    time_spent -= extra_time
                    pq.put(PQEntry(a, b - extra_time))
                else:
                    # optimize tat ca
                    S += b / a
                    time_spent -= b
        print("{:.2f}".format(S))


if __name__ == "__main__":
    main()