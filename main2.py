import pandas as pd


data = pd.read_csv('circledata.csv')
import pandas as pd


data = pd.read_csv('circledata.csv')


filtered_data = data[(data['Condition'] == 'BreathStaircase') | (data['Condition'] == 'BreathComplete')]


participants_foil = []
participants_jnd = []
participants_colors = []


for pnum in range(1, 81):

    participant_data = filtered_data[filtered_data['Pnum'] == pnum]


    foil = participant_data[' foil'].tolist()
    jnd = participant_data['JND'].tolist()
    colors = participant_data['Response'].tolist()


    participants_foil.append(foil)
    participants_jnd.append(jnd)
    participants_colors.append(colors)


for pnum in range(1, 81):
    print(f"Participant {pnum}:")
    print("foil:", participants_foil[pnum - 1])
    print("JND:", participants_jnd[pnum - 1])
    print("Response:", participants_colors[pnum - 1])
    print()

filtered_data = data[(data['Condition'] == 'BreathStaircase') | (data['Condition'] == 'BreathComplete')]


participants_foil = []
participants_jnd = []
participants_colors = []


for pnum in range(1, 81):

    participant_data = filtered_data[filtered_data['Pnum'] == pnum]


    foil = participant_data[' foil'].tolist()
    jnd = participant_data['JND'].tolist()
    colors = participant_data['Response'].tolist()


    participants_foil.append(foil)
    participants_jnd.append(jnd)
    participants_colors.append(colors)


for pnum in range(1, 81):
    print(f"Participant {pnum}:")
    print("foil:", participants_foil[pnum - 1])
    print("JND:", participants_jnd[pnum - 1])
    print("Response:", participants_colors[pnum - 1])
    print()