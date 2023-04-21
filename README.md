# Pattern-Recognition-and-Machine-Learning-PRML-
(1) The Dataset1.csv data-set has 1000 data points generated from a mixture of some distribution.

  (i) File XX is a code to determine which probabilisitic mixture could have generated this data. The EM algorithm is derived by setting the number of mixtures K = 4.           The log-likelihood is plotted in File XX.
  
    (averaged over 100 random initializations) as a function of iterations.
    
  (ii) Assume that the same data was infact generated from a mixture of Gaussians
with 4 mixtures. Implement the EM algorithm and plot the log-likelihood (averaged over 100 random initializations of the parameters) as a function of iterations.
How does the plot compare with the plot from part (i)? Provide insights that
you draw from this experiment.
iii. Run the K-means algorithm with K = 4 on the same data. Plot the objective of
K − means as a function of iterations.
iv. Among the three different algorithms implemented above, which do you think
you would choose to for this dataset and why?
(2) You are given a data-set in the file A2Q2Data train.csv with 10000 points in (R
100
, R)
(Each row corresponds to a datapoint where the first 100 components are features and
the last component is the associated y value).
i. Obtain the least squares solution wML to the regression problem using the analytical solution.
ii. Code the gradient descent algorithm with suitable step size to solve the least
squares algorithms and plot kwt − wMLk2 as a function of t. What do you
observe?
iii. Code the stochastic gradient descent algorithm using batch size of 100 and plot
kwt − wMLk2 as a function of t. What are your observations?
iv. Code the gradient descent algorithm for ridge regression. Cross-validate for various choices of λ and plot the error in the validation set as a function of λ. For
the best λ chosen, obtain wR. Compare the test error (for the test data in the
file A2Q2Data test.csv) of wR with wML. Which is better and why
