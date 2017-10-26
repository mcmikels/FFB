#Histogram of all scores so far

import FFB
import stats_FFB
import numpy
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm

#Fit the data
(mu, sigma) = norm.fit(FFB.all_scores)

bins = numpy.linspace(0, 200, 40)

y = mlab.normpdf(bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=2)

print len(FFB.all_scores)

plt.hist(FFB.all_scores, bins, normed=1, alpha = 0.5, label = "All Scores")
plt.legend(loc = 'upper right')
plt.xlabel('Scores')
plt.ylabel('N (normalized)')
plt.title(r'$\mathrm{Histogram\ of\ Scores:}\ \mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))
plt.grid(True)
plt.show()
