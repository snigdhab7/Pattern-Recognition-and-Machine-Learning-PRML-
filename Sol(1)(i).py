import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn import datasets
from sklearn.mixture import GaussianMixture
 #using sample dataset
iris = datasets.load_iris() 
X = iris.data[:, :2]
#dataset to use
df = pd.read_csv( filepath_or_buffer='D:/SnigdhaDocs/iitm/sem2/ml/Dataset1.csv', header=None, sep=',') 
df.columns=['Col1'] 
# turn it into a dataframe
#change dataset to test
d = pd.DataFrame(X)
# plot the data
plt.scatter(d[0], d[1])
gmm = GaussianMixture(n_components = 4)
 
# Fit the GMM model for the dataset
# which expresses the dataset as a
# mixture of 3 Gaussian Distribution
gmm.fit(d)
 
# Assign a label to each sample
labels = gmm.predict(d)
d['labels']= labels
d0 = d[d['labels']== 0]
d1 = d[d['labels']== 1]
d2 = d[d['labels']== 2]
 
# plot three clusters in same plot
plt.scatter(d0[0], d0[1], c ='r')
plt.scatter(d1[0], d1[1], c ='yellow')
plt.scatter(d2[0], d2[1], c ='g')

# print the converged log-likelihood value
print(gmm.lower_bound_)
 
# print the number of iterations needed
# for the log-likelihood value to converge
print(gmm.n_iter_)