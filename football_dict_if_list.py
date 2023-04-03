teams, wins, losses, draws = [], {}, {}, {}

for i in range(int(input())):
    game = input().split(';')
    
    if game[0] not in teams:
        teams.append(game[0])
    if game[-2] not in teams:
        teams.append(game[-2])
    if int(game[1]) > int(game[-1]):
        wins[game[0]] = wins.get(game[0], 0) + 1
        losses[game[-2]] = losses.get(game[-2], 0) + 1
    elif int(game[1]) < int(game[-1]):
        wins[game[-2]] = wins.get(game[-2], 0) + 1
        losses[game[0]] = losses.get(game[0], 0) + 1
    else:
        draws[game[0]] = draws.get(game[0], 0) + 1
        draws[game[-2]] = draws.get(game[2], 0) + 1

for team in teams:
    games = wins.get(team, 0) + losses.get(team, 0) + draws.get(team, 0)
    points = wins.get(team, 0) * 3 + draws.get(team, 0) * 1
    print(f'{team}:{games} {wins.get(team, 0)} {draws.get(team, 0)} {losses.get(team, 0)} {points}')
