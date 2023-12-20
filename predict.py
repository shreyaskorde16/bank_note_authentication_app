import pickle
import numpy as np

pickle_in = open('classifier.pkl', 'rb')   # will open in read binary mode
classifier = pickle.load(pickle_in)

print(f'The predicted output is {classifier.predict([[4, 3, 2, 1]])}')
