#Making plots

import FFB
import stats_FFB
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from mpl_toolkits.axes_grid.anchored_artists import AnchoredText

#define np arrays
x1 = np.array(FFB.lucky_wins)
x2 = np.array(FFB.deviation)
x3 = np.array(FFB.PPG)
x4 = np.array(FFB.PW)
x5 = np.array(FFB.adj_PW)
y1 = np.array(FFB.win_per)

#fit the data
slope_LW, intercept_LW, r_value_LW, p_value_LW, std_err_LW = stats.linregress(x1,y1)
slope_dev, intercept_dev, r_value_dev, p_value_dev, std_err_dev = stats.linregress(x2,y1)
slope_PPG, intercept_PPG, r_value_PPG, p_value_PPG, std_err_PPG = stats.linregress(x3,y1)
slope_PW, intercept_PW, r_value_PW, p_value_PW, std_err_PW = stats.linregress(x4,y1)
slope_adj_PW, intercept_adj_PW, r_value_adj_PW, p_value_adj_PW, std_err_adj_PW = stats.linregress(x5,y1)
slope_hybrid, intercept_hybrid, r_value_hybrid, p_value_hybrid, std_err_hybrid = stats.linregress(x3-x2,y1)

print "Linear Fit for Lucky Wins is"
print "y = %s x + %s" % (slope_LW,intercept_LW)
print "R^2 = %s" % r_value_LW ** 2

print "Linear Fit for Deviation is"
print "y = %s x + %s" % (slope_dev,intercept_dev)
print "R^2 = %s" % r_value_dev ** 2

print "Linear Fit for PPG is"
print "y = %s x + %s" % (slope_PPG,intercept_PPG)
print "R^2 = %s" % r_value_PPG ** 2

print "Linear Fit for PW is"
print "y = %s x + %s" % (slope_PW,intercept_PW)
print "R^2 = %s" % r_value_PW ** 2

print "Linear Fit for adj_PW is"
print "y = %s x + %s" % (slope_adj_PW,intercept_adj_PW)
print "R^2 = %s" % r_value_adj_PW ** 2

print "Linear Fit for PPG-dev is"
print "y = %s x + %s" % (slope_hybrid,intercept_hybrid)
print "R^2 = %s" % r_value_hybrid ** 2


fig1 = plt.figure()

ax1 = fig1.add_subplot(231)
ax1.scatter(x1,y1)
ax1.plot(x1,slope_LW * x1 + intercept_LW,"-")
ax1.set_title('Win% vs. LW')
at = AnchoredText("R^2 = %s" % r_value_LW ** 2,
                  prop=dict(size=5), frameon=True,
                  loc=4,
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax1.add_artist(at)

ax2 = fig1.add_subplot(232)
ax2.scatter(x2,y1)
ax2.plot(x2,slope_dev * x2 + intercept_dev,"-")
ax2.set_title('Win% vs. Dev')
at = AnchoredText("R^2 = %s" % r_value_dev ** 2,
                  prop=dict(size=5), frameon=True,
                  loc=4,
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax2.add_artist(at)

ax3 = fig1.add_subplot(233)
ax3.scatter(x3,y1)
ax3.plot(x3,slope_PPG * x3 + intercept_PPG,"-")
ax3.set_title('Win% vs. PPG')
at = AnchoredText("R^2 = %s" % r_value_PPG ** 2,
                  prop=dict(size=5), frameon=True,
                  loc=4,
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax3.add_artist(at)

ax4 = fig1.add_subplot(234)
ax4.scatter(x4,y1)
ax4.plot(x4,slope_PW * x4 + intercept_PW,"-")
ax4.set_title('Win% vs. PW')
at = AnchoredText("R^2 = %s" % r_value_PW ** 2,
                  prop=dict(size=5), frameon=True,
                  loc=4,
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax4.add_artist(at)

ax5 = fig1.add_subplot(235)
ax5.scatter(x5,y1)
ax5.plot(x5,slope_adj_PW * x5 + intercept_adj_PW,"-")
ax5.set_title('Win% vs. adj_PW')
at = AnchoredText("R^2 = %s" % r_value_adj_PW ** 2,
                  prop=dict(size=5), frameon=True,
                  loc=4,
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax5.add_artist(at)

ax6 = fig1.add_subplot(236)
ax6.scatter(x3-x2,y1)
ax6.plot(x3-x2,slope_hybrid * (x3-x2) + intercept_hybrid,"-")
ax6.set_title('Win% vs. PPG-dev')
at = AnchoredText("R^2 = %s" % r_value_hybrid ** 2,
                  prop=dict(size=5), frameon=True,
                  loc=4,
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax6.add_artist(at)

plt.tight_layout()
plt.show()
