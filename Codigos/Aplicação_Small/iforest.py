# Aplicação do iforest para o small

# %%

import pandas as pd
import matplotlib.pyplot
import seaborn as sns

from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

# %%

df = pd.read_csv("../../Dados/creditcard.csv")
df

# Explicação variáveis
# time: Number of seconds elapsed between this transaction and the first transaction in the dataset
# V1: may be result of a PCA Dimensionality reduction to protect user identities and sensitive features(v1-v28)
# Amount: Transaction amount
# Class: 1 for fraudulent transactions, 0 otherwise

# %%

features = df.columns.tolist()[2:-1]
features

# %%
