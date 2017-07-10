from random import choice

file = open('players.txt', 'r')
players = file.read().splitlines()
file.close()
teams = ['Alligators', 'Gorrillas', 'Eagles', 'Pythons', 'Wasps', 'Panthers']

team1 = []
team2 = []


def pickteam1():
    for i in range(len(players)/2):
        player = choice(players)
        print(player)
        team1.append(player)
        players.remove(player)
    return team1

def pickteam2():
    for i in range(len(players)):
        player = choice(players)
        print(player)
        team2.append(player)
        players.remove(player)
    return team2

pickteam1()
pickteam2()

team1name = choice(teams)
teams.remove(team1name)
team2name = choice(teams)
teams.remove(team2name)

print(team1name + ": " + str(team1))
print(team2name + ": " + str(team2))
