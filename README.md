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

If somebody wants to implement a much better version of this, the TLDR is that the original implementation optimizes a logistic regression. For more details on the form of the design matrix and target, take a look at `math.ipynb`.


## Important Links
Paper: [Bradley-Terry models in R: The BradleyTerry2 package](https://pdfs.semanticscholar.org/9703/5a0ed0ab764f317cf90e1c0d0a9a527145aa.pdf)

Github: https://github.com/hturner/BradleyTerry2

