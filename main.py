#----------------------------------------------------------

#   Author: Shreyas Sanjay Korde ----------------------------
#   M. Sc. Mechatronics -------------------------------------
#   Project Name: Bank Authentication App -------------------

#----------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('BankNote_Authentication.csv')
#print(df)
x = df.iloc[:, :-1]
y = df.iloc[:,-1]
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)


#print(y_train)
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(x_train, y_train)




