#Calcuates win expectancy based on pythagorean expectation

import FFB

team1 = input("What is your team?")
team2 = input("Who are you playing?")

win_prob = (FFB.pythagorean_wins(FFB.PPG_dictionary[team1],FFB.PPG_dictionary[team2],FFB.total_games))/FFB.total_games

print "You have a %s percent chance of winning. Good luck!" % (win_prob * 100)
