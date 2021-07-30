from itertools import combinations
import pandas as pd
from helper import *
import statsmodels.api as sm


def counts_to_binomial(df):
  upper = matrix_to_triangular(df, upper=True)
  lower = matrix_to_triangular(df, upper=False)
  return upper.join(lower, on=['row', 'col']).reset_index()


def btm(wins_df):
  num_players = max(wins_df.col) + 1
  design_matrix = get_design_matrix(wins_df)
  y = wins_df.wins / (wins_df.wins + wins_df.losses)
  design_matrix.columns = [f'e_{i}' for i in range(1,  num_players)] 
  formula = build_formula(design_matrix.columns)
  design_matrix.insert(0, 'y', y)
  model = sm.formula.glm(formula, family=sm.families.Binomial(), data=design_matrix).fit()
  return model


if __name__ == '__main__':
    # duplicated Example 1.2 from Bradley-Terry models in R: The BradleyTerry2 package: https://pdfs.semanticscholar.org/9703/5a0ed0ab764f317cf90e1c0d0a9a527145aa.pdf
    citations = pd.DataFrame({'Biometrika': [714, 33, 320, 284], 'CommStatist': [730, 425, 813, 276], 'JASA': [498, 68, 1072, 325], 'JRSSB': [221, 17, 142, 188]})
    citations.index = ['Biometrika', 'CommStatist', 'JASA', 'JRSSB']
    counts_df = counts_to_binomial(citations)
    print(btm(counts_df).summary())