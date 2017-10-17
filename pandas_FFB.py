#first crack at using pandas to analyze the data

import FFB
import stats_FFB
import pandas as pd
import statsmodels.formula.api as sm

#df = pd.DataFrame({"A":FFB.win_per, "B":FFB.PPG, "C":FFB.deviation})
#result = sm.ols(formula="A ~ B + C", data=df).fit()
#print result.params
#print result.summary()

df = pd.DataFrame({"A":FFB.adj_PW, "B":FFB.QB_scores, "C":FFB.RB_scores, "D":FFB.WR_scores,
    "E":FFB.TE_scores, "F":FFB.FLEX_scores, "G":FFB.DEF_scores, "H":FFB.K_scores})
result = sm.ols(formula="A ~ B + C + D + E + F + G + H", data=df).fit()
print result.params
print result.summary()

print "Coefficients: B - QB, C - RB, D - WR, E - TE, F - flex, G - DEF, H - K"
