#Calcuates win expectancy based on pythagorean expectation
#Takes team name strings, prints % chance of winning

import FFB
import stats_FFB
import numpy
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

print "Select your team and your opponent from the list below:"
for FFB.team in FFB.teams:
    print FFB.team

#Input team names
team1 = input("What is your team?")
team2 = input("Who are you playing?")

#Win probability from pythagorean wins
win_prob = (FFB.pythagorean_wins(FFB.PPG_dictionary[team1],FFB.PPG_dictionary[team2],FFB.total_games))/FFB.total_games

#Monte Carlo sim of the two teams
team1_trials = numpy.random.normal(stats_FFB.mean_dictionary[team1],stats_FFB.sigma_dictionary[team1],100000)
team2_trials = numpy.random.normal(stats_FFB.mean_dictionary[team2],stats_FFB.sigma_dictionary[team2],100000)

MC_wins = []
winning_score1 = []
losing_score1 = []
winning_score2 = []
losing_score2 = []
team1_scores = []
team2_scores = []
for score1,score2 in zip(team1_trials,team2_trials):
    team1_scores.append(score1)
    team2_scores.append(score2)
    if score1 > score2:
        MC_wins.append(score1)
        winning_score1.append(score1)
        losing_score1.append(score2)
    elif score1 < score2:
        losing_score2.append(score1)
        winning_score2.append(score2)

number_of_wins = len(MC_wins)
average_win1 = sum(winning_score1)/len(winning_score1)
average_loss1 = sum(losing_score1)/len(losing_score1)
average_win2 = sum(winning_score2)/len(winning_score2)
average_loss2 = sum(losing_score2)/len(losing_score2)

sim_dev = stats_FFB.mean_dictionary[team1] - average_win1

print "You won %s games in a 100,000 game Monte Carlo simulation." % number_of_wins
print "In the Monte Carlo, your average win was %s to %s" % (average_win1, average_loss1)
print "In the Monte Carlo, your average loss was %s to %s" % (average_win2, average_loss2)
print "You have a %s percent chance of winning, according to the Pythagorean expectation." % (win_prob * 100)

#Make histograms for each team's scores
bins = numpy.linspace(0, 200, 200)
plt.hist(team1_scores, bins, alpha = 0.5, label = team1)
plt.hist(team2_scores, bins, alpha = 0.5, label = team2)
plt.legend(loc = 'upper right')
plt.show()
