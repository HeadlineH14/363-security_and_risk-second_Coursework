# -- START OF YOUR CODERUNNER SUBMISSION CODE
# INCLUDE ALL YOUR IMPORTS HERE
import numpy as np
from scipy import stats
from dhCheck_Task1 import dhCheckCorrectness
def Task1(a, b, c, point1, number_set, prob_set, num, point2, mu, sigma, xm, alpha, point3, point4):
    #creating a triangular distribution using the scipy stats training with the lower a upper b and mode c limits 
    triangular_dist = stats.triang(c=(c-a)/(b-a), loc=a, scale=b-a)
    prob1 = triangular_dist.cdf(point1)  # Probability at point1 using cdf method of triangular distribuion 
    MEAN_t = triangular_dist.mean()       # Mean of AV
    MEDIAN_t = triangular_dist.median()   # Median of AV

    # Step 2: Calculate mean and variance of numbers of annual occurrences
    MEAN_d = np.dot(number_set, prob_set)   # Mean of annual occurrences
    VARIANCE_d = np.dot((number_set - MEAN_d)**2, prob_set)  # Variance of annual occurences

    #  PART 3 - Monte Carlo Simulation for Total Impact
    lognormal_A = stats.lognorm(s=sigma, scale=np.exp(mu)) # creates a log normal distribution 
    pareto_B = stats.pareto(b=alpha, scale=xm) # creates a pareto distribution 
    impact_A = lognormal_A.rvs(num) #generate sample sizes 'num' from the log normal distribution 
    impact_B = pareto_B.rvs(num)
    total_impact = impact_A + impact_B #calculates the total impact by summing the impacts caused by flaws A and B 

    # PART 3.1 - Probability that total impact is greater than point2
    prob2 = np.sum(total_impact > point2) / num
    
    # PART 3.2 - Probability that total impact is between point3 and point4
    prob3 = np.sum((total_impact > point3) & (total_impact < point4)) / num

    # PART 4 - Calculation of ALE
    EF = prob2 # assigns the probabillity 'prob2' as the exposure factor EF for the calcualtion of ALE
    ALE = MEAN_d * (MEDIAN_t * EF) # calculates the ALE using the mean of the number of anunual occurances
    
    return (prob1, MEAN_t, MEDIAN_t, MEAN_d, VARIANCE_d, prob2, prob3, ALE)

# -- END OF YOUR CODERUNNER SUBMISSION CODE
