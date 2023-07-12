from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import numpy as np


participants_foil = [
    [6.6, 6.2, 5.8, 6, 6, 4, 5.9, 5.9, 4.1, 4.2, 5.85, 4.15, 4.15, 4.15],
    [3.5, 3.2, 3.8, 4, 4.1, 3.9, 3.7, 3.6, 3.4, 3.5, 3.3, 3.2, 3.1, 3],

]

participants_jnd = [
    [-1, -1, -1, 0.8, 0.8, 0.8, 1, 1, 1, 1, 0.8, 0.8, 0.8, 0.85],
    [-1, -1, -1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],

]

participants_colors = [
    [2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2],
    [1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2],

]


participants_foil = np.array(participants_foil)
participants_jnd = np.array(participants_jnd)
participants_colors = np.array(participants_colors)


for i in range(participants_foil.shape[0]):

    foil = participants_foil[i]
    jnd = participants_jnd[i]
    colors = participants_colors[i]


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

    print("Participant", i+1)
    print("Predicted JND:", predicted_jnd)
    print("Predicted Response:", predicted_color)
    print()
















































































































































