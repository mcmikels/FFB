# Fantasy Football Analysis
#I'm a n00b at this, so feel free to change and/or tell me I'm a n00b
#This just goes PPG and unadjusted PW for now, trying to figure out the best way
# to get the luck information in

import csv

#import league data from league.data.csv
with open('league_data.csv','rU') as csvfile:
    reader = csv.reader(csvfile, delimiter= ",")
    teams = []
    points_for = []
    points_against = []
    wins = []
    losses = []
    deviation = []
    for row in reader:
        team = row[0]
        PF = row[1]
        PA = row[2]
        win = row[3]
        loss = row[4]
        dev = row[5]

        teams.append(team)
        points_for.append(PF)
        points_against.append(PA)
        wins.append(win)
        losses.append(loss)
        deviation.append(dev)

        #convert strings to floats or ints
        points_for = map(float, points_for)
        points_against = map(float, points_against)
        wins = map(int, wins)
        losses = map(int, losses)
        deviation = map(float, deviation)

#create record dictionary
record = zip(wins,losses)
record_dictionary = dict(zip(teams,record))

#Define variables
exponent = 5.729 #pythagorean exponent
total_games = 3.0 #total games (will need to figure out a better way for this)
number_of_teams = len(teams) #total teams

#points per game function
def points_per_game(points_scored, games):
    per_game = points_scored/total_games
    return per_game

#calculate points per game and store it
PPG = [points_per_game(points_for[i],total_games) for i in range(0,12)]
PPG_dictionary = dict(zip(teams,PPG))

#pythagorean wins function
def pythagorean_wins(points_scored,points_given,total_games):
    pythag = ((points_scored ** exponent)/(points_scored ** exponent + points_given ** exponent))\
     * total_games
    return pythag

#calculate PW and store it
PW = [pythagorean_wins(points_for[i],points_against[i],total_games) for i in range(0,12)]
PW_dictionary = dict(zip(teams,PW))
#for teams,PW in PW_dictionary.items():
    #print ('{} {}'.format(teams,PW))

#difference function
def difference(wins,pythag_wins):
    diff = wins - pythag_wins
    return diff

#calculate adjusted pythagorean wins function
def adjusted_pythagorean_wins(points_scored,points_given,devs,total_games):
    adj_pythag = ((points_scored ** exponent)/(points_scored ** exponent + (points_given - devs * total_games) ** exponent))\
    * total_games
    return adj_pythag

#calculate adjusted PW and store it
adj_PW = [adjusted_pythagorean_wins(points_for[i],points_against[i],deviation[i],total_games) for i in range(0,12)]
adj_PW_dictionary = dict(zip(teams,adj_PW))

#calculate lucky wins and store it
lucky_wins = [difference(wins[i],adj_PW[i]) for i in range(0,12)]
lucky_wins_dictionary = dict(zip(teams,lucky_wins))

#for teams,lucky_wins in lucky_wins_dictionary.items():
    #print ('{} {}'.format(teams,lucky_wins))
