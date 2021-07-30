# py_bradleyterry2

Barebones re-implementation of of the BradleyTerry2 package in R (links down below). I am not affiliated with the original author, I just needed some of the functionality for a Kaggle competition (CommonLit Readability). This implementation does not include home/away advantage or modeling with explanatory variables. It also outputs slightly different coefficients than the R package (no idea why).

Python output on the `citations` dataset (Example 1.2 of below paper):

```
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
e_1           -2.8813      2.640     -1.091      0.275      -8.056       2.293
e_2           -0.4893      1.618     -0.302      0.762      -3.660       2.681
e_3            0.2561      1.619      0.158      0.874      -2.917       3.429

```

R Output:

```
Coefficients:
journalComm Statist          journalJASA        journalJRSS-B  
            -2.9491              -0.4796               0.2690
```

If somebody wants to implement a much better version of this, the TLDR is that the original implementation optimizes a logistic regression.

The design matrix is given as follows. If there are $N$ players, then the design matrix $M$ has shape ${N \choose 2} \times N$. First, we order the combinations lexicographically, that is: $$\{1,2\}, \{1,3\}, \dots, \{N-1, N\}$$ If $C_i = \{a, b\}$, then $M[i][a] = 1$ and $M[i][b] = -1$. All other entries in the row are set to 0. Afterwards, we delete the first column so that $M$ now has shape ${N \choose 2} - 1 \times N$. This ensures that the coefficient of the first player $\beta_1$ is 0. The other common constraint is $\sum \beta_i = 1$. The reason why a constraint is needed is because the optimization problem is scale invariant, so we need to pick some reference. 

The response $y$ is the ratio of wins. For example, if player 1 won against player 2 $w$ times and lost $l$ times, then $$y[0] = \frac{w}{w + l}$$

Repeat this for all combinations $C_i$ to form $y$.


## Important Links
Paper: [Bradley-Terry models in R: The BradleyTerry2 package](https://pdfs.semanticscholar.org/9703/5a0ed0ab764f317cf90e1c0d0a9a527145aa.pdf)

Github: https://github.com/hturner/BradleyTerry2

