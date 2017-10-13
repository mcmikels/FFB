# FFB
First stab at the code for analyzing our fantasy football league. It takes the file league_data.csv. Should calculate points per game and unadjusted pythagorean wins. Both are stored as dictionaries.

Update 10/2/17
Currently two other programs, win_exp takes inputs of the strings of team names, gives the percent chance the first entered team has of defeating the second entered team. output_data spits out a csv file of PPG and adjusted PW by team. It needs some more work; the file formatting is ugly. But it works.

FFB also now calcuates adjusted PW, calculates Lucky Wins and stores stores a dictionary of each team's record. Right now, the league_data file has to by manually updated with the "deviation per game," which is what the program uses to calcuate adjusted PW and Lucky Wins. I'm currently trying to figure out a way to loop through game results to calcuate this value.


Update 10/6/17

Updated FFB to take two files, league_data.csv and weeklyresults.csv, and calculates deviation from that - no need to manually enter it into the input file. It's not elegant, but it works. Program spits out the lucky wins for each team.


Update 10/13/17

Updated FFB to find total games automatically for PPG calculations, having issues with the int, so that still has to be entered manually. Updated win_exp to do a Monte Carlo sim as well (10,000 games). The code stats_FFB calculates various stats needed in other programs. The program plots does linear fits for various variables and win percentage, then spits out a plot of the fits with R^2. It also outputs the equations in the terminal.

Also working on more advanced regressions using pandas, but they need more work. They're forthcoming.
