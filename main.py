from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import numpy as np


foil = [6.6, 6.2, 5.8, 6, 6, 4, 5.9, 5.9, 4.1, 4.2, 5.85, 4.15, 4.15, 4.15]
jnd = [-1, -1, -1, 0.8, 0.8, 0.8, 1, 1, 1, 1, 0.8, 0.8, 0.8, 0.85]
colors = [2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2]


X = np.array(foil).reshape(-1, 1)
y_jnd = np.array(jnd)
y_color = np.array(colors)


regressor = RandomForestRegressor()
regressor.fit(X, y_jnd)


classifier = RandomForestClassifier()
classifier.fit(X, y_color)


new_foil = np.array([4.5, 5.0, 5.5])
predicted_jnd = regressor.predict(new_foil.reshape(-1, 1))
predicted_color = classifier.predict(new_foil.reshape(-1, 1))

print("Predicted JND:", predicted_jnd)
print("Predicted Response:", predicted_color)















































































































































