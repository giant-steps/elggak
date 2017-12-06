


import pandas as pd

import os
os.getcwd()

print(os.path.exists('Documents\Code\elggak\data_dev.csv'))

print("passed")

df = pd.read_csv('Documents\Code\elggak\data_dev.csv')

print(df.sheet_names)

