import numpy as np

gametime = np.array([4.6, 4.9, 7, 1.7, 5.6, 1.2, 0.1, 7.9, 5.2, 3.4,4.2, 0.1, 4.7, 1.9, 3.4, 4.8, 5.2, 1.5, 1, 7], dtype=float)
examscore = np.array([44, 43, 2, 79, 21, 83, 78, 3, 31, 44,38, 83, 47, 69, 49, 34, 34, 68, 78, 8], dtype=float)

import matplotlib.pyplot as plt

plt.scatter(gametime,examscore)
plt.show()

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

model=Sequential([Dense(units=1,input_shape=[1])])

model.compile(optimizer='sgd', loss='mean_squared_error')

model.fit(gametime/24, examscore/100, epochs=8000)

[[w]], [b] = model.layers[0].get_weights()
print( f"Learned parameters: w = {w}, b = {b}")

plt.plot(gametime, examscore, 'ro', label = 'original')
examscorepredict = model.predict(gametime/24)*100
plt.plot(gametime, examscorepredict, label = 'predict')
plt.legend()
plt.show()

timedata1 = np.array([5.9, 5.5, 4.7, 4.2, 1.1])

examscorepredict = model.predict(timedata1/24)*100

for i in range(len(examscorepredict)):
  print("Game time: "+str(timedata1[i])+" => Predicted exam score: "+str(examscorepredict[i]))
