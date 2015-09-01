import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

plt.figure()
loansData.boxplot(column='Amount.Requested')
plt.savefig("Amount.Requested_boxplot.png")

plt.figure()
loansData.hist(column='Amount.Requested')
plt.savefig("Amount.Requested_histogram.png")

import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("Amount.Requested_probplot.png")