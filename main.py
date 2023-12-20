#----------------------------------------------------------

#   Author: Shreyas Sanjay Korde ----------------------------
#   M. Sc. Mechatronics -------------------------------------
#   Project Name: Bank Authentication App -------------------

#----------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

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
y_pred = classifier.predict(x_test)


accuracy = accuracy_score(y_test, y_pred)
#print(f'Accuracy after applying Random forest classifier is {"{:.2%}".format(accuracy)}')
print('\n')
print('*'*10)
print(f'Accuracy after applying Random forest classifier is {accuracy:.2%}')
print('-'*10)
print('\n')

