'''
Basic jackknife estimation - mean

Jackknife resampling is an older procedure, which isn't used as often compared as bootstrapping. However, it's still useful to know how to run a basic jackknife estimation procedure. In this first exercise, we will calculate the jackknife estimate for the mean. Let's return to the wrench factory.

You own a wrench factory and want to measure the average length of the wrenches to ensure that they meet some specifications. Your factory produces thousands of wrenches every day, but it's infeasible to measure the length of each wrench. However, you have access to a representative sample of 100 wrenches. Let's use jackknife estimation to get the average lengths.

Examine the variable wrench_lengths in the shell.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

# Default set by DataCamp
wrench_lengths = np.array([
        8.91436940, 10.99734545, 10.28297850,  8.49370529,  9.42139975,
       11.65143654,  7.57332076,  9.57108737, 11.26593626,  9.13325960,
        9.32111385,  9.90529103, 11.49138963,  9.36109800,  9.55601804,
        9.56564872, 12.20593008, 12.18678609, 11.00405390, 10.38618640,
       10.73736858, 11.49073203,  9.06416613, 11.17582904,  8.74611933,
        9.36224850, 10.90710520,  8.57131930,  9.85993128,  9.13824510,
        9.74438063,  7.20141089,  8.22846690,  9.30012277, 10.92746243,
        9.82636432, 10.00284592, 10.68822271,  9.12046366, 10.28362732,
        9.19463348,  8.27233051,  9.60910021, 10.57380586, 10.33858905,
        9.98816951, 12.39236527, 10.41291216, 10.97873601, 12.23814334,
        8.70591468,  8.96121179, 11.74371223,  9.20193726, 10.02968323,
       11.06931597, 10.89070639, 11.75488618, 11.49564414, 11.06939267,
        9.22729129, 10.79486267, 10.31427199,  8.67373454, 11.41729905,
       10.80723653, 10.04549008,  9.76690794,  8.80169886, 10.19952407,
       10.46843912,  9.16884502, 11.16220405,  8.90279695,  7.87689965,
       11.03972709,  9.59663396,  9.87397041,  9.16248328,  8.39403724,
       11.25523737,  9.31113102, 11.66095249, 10.80730819,  9.68524185,
        8.91409760,  9.26753801,  8.78747687, 12.08711336, 10.16444123,
       11.15020554,  8.73264795, 10.18103513, 11.17786194,  9.66498924,
       11.03111446,  8.91543209,  8.63652846, 10.37940061,  9.62082357])

# Randomly generated example similar to DataCamp
#wrench_lengths = np.random.rand(100)*4 + 8

'''
INSTRUCTIONS

*   Get a jackknife sample by iteratively leaving one observation out of wrench_lengths and assigning it to jk_sample.
*   Calculate the mean of jk_sample and append it to mean_lengths.
*   Finally, calculate the mean of mean_lengths as the jackknife estimate.
'''

# Leave one observation out from wrench_lengths to get the jackknife sample and store the mean length
mean_lengths, n = [], len(wrench_lengths)
index = np.arange(n)

for i in range(n):
    jk_sample = wrench_lengths[index != i]
    mean_lengths.append(jk_sample.mean())

# The jackknife estimate is the mean of the mean lengths from each sample
mean_lengths = np.array(mean_lengths)
print("Jackknife estimate of the mean = {}".format(mean_lengths.mean()))