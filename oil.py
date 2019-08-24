import tensorflow as tf
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data = pd.read_excel('Simulation Data (1).xlsx')

X_train, X_test, y_train, y_test =train_test_split(data[['GOR', 'Oil gravity', 'Gas gravity', 'T']], data.Pb)
ss=StandardScaler()
X_train=ss.fit_transform(X_train)
X_test=ss.transform(X_test)

print(X_test.shape)
print(X_train.shape)