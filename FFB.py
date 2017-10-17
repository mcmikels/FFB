# Fantasy Football Analysis
#I'm a n00b at this, so feel free to change and/or tell me I'm a n00b
#This just goes PPG and unadjusted PW for now, trying to figure out the best way
# to get the luck information in
#Now I have each teams weekly points in, now need to figure out how to
# cycle through the matchups

import csv
import numpy
import operator

#Define variables
exponent = 5.729 #pythagorean exponent
total_games = 6.0

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
        #dev = row[5] not needed anymore

        teams.append(team)
        points_for.append(PF)
        points_against.append(PA)
        wins.append(win)
        losses.append(loss)
        #deviation.append(dev) not needed anymore

        #convert strings to floats or ints
        points_for = map(float, points_for)
        points_against = map(float, points_against)
        wins = map(int, wins)
        losses = map(int, losses)
        #deviation = map(float, deviation) not needed anymore

#get position scores
with open('position_data.csv','rU') as csvfile:
    reader = csv.reader(csvfile, delimiter= ",")
    QB_scores = []
    RB_scores = []
    WR_scores = []
    TE_scores = []
    FLEX_scores = []
    DEF_scores = []
    K_scores = []
    #don't need team strings extracted
    for row in reader:
        QB = row[1]
        RB = row[2]
        WR = row[3]
        TE = row[4]
        FLEX = row[5]
        DEF = row[6]
        KR = row[7]

        QB_scores.append(QB)
        RB_scores.append(RB)
        WR_scores.append(WR)
        TE_scores.append(TE)
        FLEX_scores.append(FLEX)
        DEF_scores.append(DEF)
        K_scores.append(KR)

        QB_scores = map(float, QB_scores)
        RB_scores = map(float, RB_scores)
        WR_scores = map(float, WR_scores)
        TE_scores = map(float, TE_scores)
        FLEX_scores = map(float, FLEX_scores)
        DEF_scores = map(float, DEF_scores)
        K_scores = map(float, K_scores)

#win percentage function
def win_percentage(games_won):
    percent = games_won/total_games
    return percent

win_per = [win_percentage(wins[i]) for i in range(0,12)]
win_per_dictionary = dict(zip(teams,win_per))

#print win_per_dictionary

#Open the results file and gets the scores for each team
with open('weekly_results.csv','rU') as csvfile:
    reader = csv.reader(csvfile, delimiter= ",")
    righteous_in_wrath_scores = []
    toms_shady_weinerz_scores = []
    fournettecate_scores = []
    big_ol_TDs_scores = []
    equipmunk_managers_scores = []
    fhqwhgads_scores = []
    butts_scores = []
    lick_my_quintorris_scores = []
    menstrual_krampus_scores = []
    stranger_in_the_alps_scores = []
    mother_of_dragons_scores = []
    wit_and_creativity_scores = []
    for row in reader:
        RIW_score = row[0]
        TSW_score = row[1]
        F_score = row[2]
        BOT_score = row[3]
        EM_score = row[4]
        FHQ_score = row[5]
        butt_score = row[6]
        LMQ_score = row[7]
        MK_score = row[8]
        SITA_score = row[9]
        MOD_score = row[10]
        WAC_score = row[11]

        righteous_in_wrath_scores.append(RIW_score)
        toms_shady_weinerz_scores.append(TSW_score)
        fournettecate_scores.append(F_score)
        big_ol_TDs_scores.append(BOT_score)
        equipmunk_managers_scores.append(EM_score)
        fhqwhgads_scores.append(FHQ_score)
        butts_scores.append(butt_score)
        lick_my_quintorris_scores.append(LMQ_score)
        menstrual_krampus_scores.append(MK_score)
        stranger_in_the_alps_scores.append(SITA_score)
        mother_of_dragons_scores.append(MOD_score)
        wit_and_creativity_scores.append(WAC_score)


#Get rid of the team name in the list
del righteous_in_wrath_scores[0]
del toms_shady_weinerz_scores[0]
del fournettecate_scores[0]
del big_ol_TDs_scores[0]
del equipmunk_managers_scores[0]
del fhqwhgads_scores[0]
del butts_scores[0]
del lick_my_quintorris_scores[0]
del menstrual_krampus_scores[0]
del stranger_in_the_alps_scores[0]
del mother_of_dragons_scores[0]
del wit_and_creativity_scores[0]

#convert to floats
righteous_in_wrath_scores = map(float, righteous_in_wrath_scores)
toms_shady_weinerz_scores = map(float,toms_shady_weinerz_scores)
fournettecate_scores = map(float,fournettecate_scores)
big_ol_TDs_scores = map(float,big_ol_TDs_scores)
equipmunk_managers_scores = map(float,equipmunk_managers_scores)
fhqwhgads_scores = map(float,fhqwhgads_scores)
butts_scores = map(float,butts_scores)
lick_my_quintorris_scores = map(float,lick_my_quintorris_scores)
menstrual_krampus_scores = map(float,menstrual_krampus_scores)
stranger_in_the_alps_scores = map(float,stranger_in_the_alps_scores)
mother_of_dragons_scores = map(float,mother_of_dragons_scores)
wit_and_creativity_scores = map(float,wit_and_creativity_scores)

#define number of games variables
tot_games = len(righteous_in_wrath_scores)

#make array of scores
a = numpy.array(righteous_in_wrath_scores) #0
b = numpy.array(toms_shady_weinerz_scores) #1
c = numpy.array(fournettecate_scores) #2
d = numpy.array(big_ol_TDs_scores) #3
e = numpy.array(equipmunk_managers_scores) #4
f = numpy.array(fhqwhgads_scores) #5
g = numpy.array(butts_scores) #6
h = numpy.array(lick_my_quintorris_scores) #7
i = numpy.array(menstrual_krampus_scores) #8
j = numpy.array(stranger_in_the_alps_scores) #9
k = numpy.array(mother_of_dragons_scores) #10
l = numpy.array(wit_and_creativity_scores) #11

#score_matrix in form of (week,team) gives score
score_matrix = numpy.column_stack((a,b,c,d,e,f,g,h,i,j,k,l))

#Define schedules
RIW_schedule = [8,11,3,7,9,2,10,8,1,4,11,3,2]
TSW_schedule = [7,9,6,10,11,5,4,7,0,8,9,6,5]
four_schedule = [3,8,10,4,5,0,11,3,6,7,8,10,0]
BOT_schedule = [2,10,0,5,6,11,8,2,7,9,10,0,11]
EM_schedule = [5,6,7,2,10,9,1,5,11,0,6,7,9]
FHQ_schedule = [4,7,9,3,2,1,6,4,10,11,7,10,1]
butts_schedule = [9,4,1,8,3,7,5,9,2,10,4,1,7]
LMQ_schedule = [1,5,4,0,8,6,9,1,3,2,5,4,6]
MK_schedule = [0,2,11,6,7,10,3,0,9,1,2,11,10]
SITA_schedule = [6,1,5,11,0,4,7,6,8,3,1,5,4]
MOD_schedule = [11,3,2,1,4,8,0,11,5,6,3,2,8]
WAC_schedule = [10,0,8,9,1,3,2,10,4,5,0,8,3]

#get each team's opponent's score by week
def RIW_opponent_score(week):
    opponent_score = score_matrix[week][RIW_schedule[week]]
    return opponent_score

def TSW_opponent_score(week):
    opponent_score = score_matrix[week][TSW_schedule[week]]
    return opponent_score

def four_opponent_score(week):
    opponent_score = score_matrix[week][four_schedule[week]]
    return opponent_score

def BOT_opponent_score(week):
    opponent_score = score_matrix[week][BOT_schedule[week]]
    return opponent_score

def EM_opponent_score(week):
    opponent_score = score_matrix[week][EM_schedule[week]]
    return opponent_score

def FHQ_opponent_score(week):
    opponent_score = score_matrix[week][FHQ_schedule[week]]
    return opponent_score

def butts_opponent_score(week):
    opponent_score = score_matrix[week][butts_schedule[week]]
    return opponent_score

def LMQ_opponent_score(week):
    opponent_score = score_matrix[week][LMQ_schedule[week]]
    return opponent_score

def MK_opponent_score(week):
    opponent_score = score_matrix[week][MK_schedule[week]]
    return opponent_score

def SITA_opponent_score(week):
    opponent_score = score_matrix[week][SITA_schedule[week]]
    return opponent_score

def MOD_opponent_score(week):
    opponent_score = score_matrix[week][MOD_schedule[week]]
    return opponent_score

def WAC_opponent_score(week):
    opponent_score = score_matrix[week][WAC_schedule[week]]
    return opponent_score

#create record dictionary
record = zip(wins,losses)
record_dictionary = dict(zip(teams,record))

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

#calculate each team's weekly deviation, put it in a list
RIW_dev = []
TSW_dev = []
four_dev = []
BOT_dev = []
EM_dev = []
FHQ_dev = []
butts_dev = []
LMQ_dev = []
MK_dev = []
SITA_dev = []
MOD_dev = []
WAC_dev = []
for n in range(tot_games):
    RIW_week_dev = RIW_opponent_score(n) - PPG[RIW_schedule[n]]
    TSW_week_dev = TSW_opponent_score(n) - PPG[TSW_schedule[n]]
    four_week_dev = four_opponent_score(n) - PPG[four_schedule[n]]
    BOT_week_dev = BOT_opponent_score(n) - PPG[BOT_schedule[n]]
    EM_week_dev = EM_opponent_score(n) - PPG[EM_schedule[n]]
    FHQ_week_dev = FHQ_opponent_score(n) - PPG[FHQ_schedule[n]]
    butts_week_dev = butts_opponent_score(n) - PPG[butts_schedule[n]]
    LMQ_week_dev = LMQ_opponent_score(n) - PPG[LMQ_schedule[n]]
    MK_week_dev = MK_opponent_score(n) - PPG[MK_schedule[n]]
    SITA_week_dev = SITA_opponent_score(n) - PPG[SITA_schedule[n]]
    MOD_week_dev = MOD_opponent_score(n) - PPG[MOD_schedule[n]]
    WAC_week_dev = WAC_opponent_score(n) - PPG[WAC_schedule[n]]
    RIW_dev.append(RIW_week_dev)
    TSW_dev.append(TSW_week_dev)
    four_dev.append(four_week_dev)
    BOT_dev.append(BOT_week_dev)
    EM_dev.append(EM_week_dev)
    FHQ_dev.append(FHQ_week_dev)
    butts_dev.append(butts_week_dev)
    LMQ_dev.append(LMQ_week_dev)
    MK_dev.append(MK_week_dev)
    SITA_dev.append(SITA_week_dev)
    MOD_dev.append(MOD_week_dev)
    WAC_dev.append(WAC_week_dev)

mean_RIW_dev = sum(RIW_dev)/len(RIW_dev)
mean_TSW_dev = sum(TSW_dev)/len(TSW_dev)
mean_four_dev = sum(four_dev)/len(four_dev)
mean_BOT_dev = sum(BOT_dev)/len(BOT_dev)
mean_EM_dev = sum(EM_dev)/len(EM_dev)
mean_FHQ_dev = sum(FHQ_dev)/len(FHQ_dev)
mean_butts_dev = sum(butts_dev)/len(butts_dev)
mean_LMQ_dev = sum(LMQ_dev)/len(LMQ_dev)
mean_MK_dev = sum(MK_dev)/len(MK_dev)
mean_SITA_dev = sum(SITA_dev)/len(SITA_dev)
mean_MOD_dev = sum(MOD_dev)/len(MOD_dev)
mean_WAC_dev = sum(WAC_dev)/len(WAC_dev)

#list with each team's opponent's deviation
deviation = [mean_RIW_dev,mean_TSW_dev,mean_four_dev,mean_BOT_dev,mean_EM_dev,
mean_FHQ_dev,mean_butts_dev,mean_LMQ_dev,mean_MK_dev,mean_SITA_dev,mean_MOD_dev,
mean_WAC_dev]

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

#print "Lucky wins"
#for teams,lucky_wins in lucky_wins_dictionary.items():
#    print ('{} {}'.format(teams,lucky_wins))

print "FFB done"
