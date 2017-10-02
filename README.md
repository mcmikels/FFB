# FFB
First stab at the code for analyzing our fantasy football league. It takes the file league_data.csv. Should calculate points per game and unadjusted pythagorean wins. Both are stored as dictionaries.

Update 10/2/17
Currently two other programs, win_exp takes inputs of the strings of team names, gives the percent chance the first entered team has of defeating the second entered team. output_data spits out a csv file of PPG and adjusted PW by team. It needs some more work; the file formatting is ugly. But it works.

FFB also now calcuates adjusted PW, calculates Lucky Wins and stores stores a dictionary of each team's record. Right now, the league_data file has to by manually updated with the "deviation per game," which is what the program uses to calcuate adjusted PW and Lucky Wins. I'm currently trying to figure out a way to loop through game results to calcuate this value.

