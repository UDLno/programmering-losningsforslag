import random

num_players = int(input("Antall spillere: "))
darts_per_round = int(input("Antall piler per runde: "))
num_rounds = 5
scores = [0 for i in range(num_players)]
print(scores)
for r in range(num_rounds):
    print("Runde", r+1)
    for p in range(len(scores)):
        print("Spiller", p+1, "går opp til linja")
        for d in range(darts_per_round):
            score = random.randint(0, 50)
            scores[p] += score
            print("Spiller", p + 1, "kastet", score, "og har nå", scores[p], "poeng")
    print("-----------------")

max = 0
leader = -1
for i in range(len(scores)):
    if scores[i] > max:
        max = scores[i]
        leader = i

print("Spiller", leader+1, "vant med", max, "poeng")
print(scores)