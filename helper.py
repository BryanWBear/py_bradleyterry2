import pandas as pd
import numpy as np

def matrix_to_triangular(df, upper):
  if upper:
    mask = np.triu
    new_cols = ['row','col','wins']
  else:
    mask = np.tril
    new_cols = ['col', 'row', 'losses']
  df.columns = range(len(df))
  df.index = range(len(df))
  counts_df = df.where(mask(np.ones(df.shape)).astype(np.bool))
  counts_df = counts_df.stack().reset_index()
  counts_df.columns = new_cols
  counts_df = counts_df[counts_df.row != counts_df.col]
  counts_df.set_index(['row', 'col'], inplace=True)
  return counts_df
  
def get_design_matrix(wins_df):  
  num_players = max(wins_df.col) + 1
  row_idx = np.expand_dims(wins_df.row, axis=1)
  col_idx = np.expand_dims(wins_df.col, axis=1)
  df_length = len(wins_df)
  design_matrix = np.zeros((df_length, num_players))
  np.put_along_axis(design_matrix, row_idx, 1, axis=1)
  np.put_along_axis(design_matrix, col_idx, -1, axis=1)
  return pd.DataFrame(design_matrix[:, 1:]) # remove reference row.

def build_formula(column_names):
  return 'y ~ ' + ' + '.join(column_names) + ' - 1'