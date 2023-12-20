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