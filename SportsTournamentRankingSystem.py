teams = []

count = int(input("Number of teams: "))

for i in range(count):
    name = input("Team name: ")
    wins = int(input("Wins: "))
    draws = int(input("Draws: "))
    score_difference = int(input("Score difference: "))
    points = wins * 3 + draws
    teams.append((points, score_difference, name))

teams.sort(key=lambda team: (-team[0], -team[1]))

for rank, (points, difference, name) in enumerate(teams, start=1):
    print(rank, name, "Points:", points)