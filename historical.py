#Historical Analysis
# The pythagorean function is win percent = PF^n/(PF^n + PA^n), this can be
# rewritten as win perecent = 1/(1+(PA/PF)^n)
#to get this in a form to fit, rewrite as (1/win percent) - 1 = (PA/PF)^n
import csv
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#get historical data
with open('historical.csv','rU') as csvfile:
    reader = csv.reader(csvfile, delimiter= ",")
    points_for = []
    points_against = []
    wins = []
    losses = []
    deviation = []
    for row in reader:
        win = row[0]
        loss = row[1]
        PF = row[2]
        PA = row[3]

        points_for.append(PF)
        points_against.append(PA)
        wins.append(win)
        losses.append(loss)

        #convert strings to floats or ints
        points_for = map(float, points_for)
        points_against = map(float, points_against)
        wins = map(float, wins)
        losses = map(float, losses)

#Calculate win percentage
win_per = []
for win,loss in zip(wins,losses):
    win_percent = win/(win + loss)
    win_per.append(win_percent)

#Define x and y data
x_data = []
for pf,pa in zip(points_for,points_against):
    x_point = pa/pf
    if x_point > 1.8:
        x_point = 1
    x_data.append(x_point)

y_data = []
for game in win_per:
    if game > 0:
        y_point = (1/game) - 1
    if game == 0:
        y_point = 0
    y_data.append(y_point)

#fit function
def fit(x,exp):
    return x ** exp

popt, pcov = curve_fit(fit, x_data, y_data, p0=5)

print popt, pcov

x_plot = np.linspace(0.6, 1.8, len(points_for))

plt.scatter(x_data, y_data, label='data')
plt.plot(x_plot, fit(x_plot, *popt), "-", label=popt)
plt.plot(x_plot, fit(x_plot, 5.729), "-", label=5.729)
plt.legend()
plt.show()
