# Pattern-Recognition-and-Machine-Learning-PRML-
<b>(1)</b> The <i>"Dataset1.csv"</i> data-set has 1000 data points generated from a mixture of some distribution.
<p>
  <b>(i)</b> File <i>"Sol(1)(i).py"</i> is a code to determine which probabilisitic mixture could have generated this data. The EM algorithm is derived by setting the       number of mixtures K = 4. The log-likelihood is plotted below. [averaged over 100 random initializations as a function of iterations]
  </p>
  
  ![image](https://user-images.githubusercontent.com/62890614/233840589-a49a7481-d081-47fc-a9df-0eb0e6a71350.png)


  <b>(ii)</b> Assuming that the data was generated from a mixture of Gaussians with 4 mixtures. File <i>"Sol(1)(ii).py"</i> implements an EM algorithm and plot the log        likelihood (averaged over 100 random initializations of the parameters) as a function of iterations.
  ![image](https://user-images.githubusercontent.com/62890614/233840691-a2750217-4bee-470e-982f-6bd33ded6b07.png)
  ![image](https://user-images.githubusercontent.com/62890614/233840719-8f86dc65-1fe6-46a7-9e95-bea032b85883.png)
  ![image](https://user-images.githubusercontent.com/62890614/233840734-b419dd11-58b6-45d6-b267-52f3cd2619e5.png)
  
  <b>(iii)</b> File <i>"Sol(1)(iii).py"</i> runs the K-means algorithm with K = 4 on the same data. Plot the objective of K − means as a function of iterations.
  
  <b>In this dataset, I found EM and that too the exponential one is providing to be better suited.</b>
 </p>
 <p>
<b>(2)</b> The <i>"Dataset2.csv"</i> data-set has 10000 points in (R100, R) (Each row corresponds to a datapoint where the first 100 components are features and the        last component is the associated y value).
  <p>
  <b>(i)</b> File <i>"Sol(2)(i).py"</i> codes the gradient descent algorithm with suitable step size to solve the least squares algorithms and plot kwt − wMLk2 as a      function of t.
  ![image](https://user-images.githubusercontent.com/62890614/233841678-b98ebc28-f387-40ec-8bf3-716d2ac8390c.png)

  
iii. Code the stochastic gradient descent algorithm using batch size of 100 and plot
kwt − wMLk2 as a function of t. What are your observations?
iv. Code the gradient descent algorithm for ridge regression. Cross-validate for various choices of λ and plot the error in the validation set as a function of λ. For
the best λ chosen, obtain wR. Compare the test error (for the test data in the
file A2Q2Data test.csv) of wR with wML. Which is better and why
    </p>
</p>
