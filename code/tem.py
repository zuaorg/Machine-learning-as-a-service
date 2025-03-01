import pandas as pd

df1 = pd.read_csv("../data/train_data/mlaas_train.csv")
df2 = pd.read_csv("../data/train_data/flaringar_training_sample.csv")

print(df1.dtypes)
