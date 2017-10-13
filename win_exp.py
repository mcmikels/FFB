#Calcuates win expectancy based on pythagorean expectation
#Takes team name strings, prints % chance of winning

import FFB
import stats_FFB
import numpy

team1 = input("What is your team?")
team2 = input("Who are you playing?")

win_prob = (FFB.pythagorean_wins(FFB.PPG_dictionary[team1],FFB.PPG_dictionary[team2],FFB.total_games))/FFB.total_games

team1_trials = numpy.random.normal(stats.mean_dictionary[team1],stats.sigma_dictionary[team1],10000)
team2_trials = numpy.random.normal(stats.mean_dictionary[team2],stats.sigma_dictionary[team2],10000)

MC_wins = []
for score1,score2 in zip(team1_trials,team2_trials):
    if score1 > score2:
        MC_wins.append(score1)

number_of_wins = len(MC_wins)

print "You won %s games in a 10,000 game Monte Carlo simulation." % number_of_wins

print "You have a %s percent chance of winning, according to the Pythagorean expectation." % (win_prob * 100)
