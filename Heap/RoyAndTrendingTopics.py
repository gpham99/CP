class Topic:
    def __init__(self, id, new_z_score, z_score_change):
        self.id = id
        self.new_z_score = new_z_score
        self.z_score_change = z_score_change

def main():
    r = []
    score = {
        "P": 50,
        "L": 5,
        "C": 10,
        "S": 20
    }
    N = int(input())
    for i in range(N):
        id, Z, P, L, C, S = map(int, input().split())
        new_z_score = P * score["P"] + L * score["L"] + C * score["C"] + S * score["S"]
        z_score_change = new_z_score - Z
        r.append(Topic(id, new_z_score, z_score_change))
    # sort r on z_score_change
    r.sort(key=lambda x: (x.z_score_change, x.id), reverse=True)
    
    for i in range(5):
        print(r[i].id, r[i].new_z_score)

if __name__ == "__main__":
    main()