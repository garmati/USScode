import csv


with open('circledata.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)


    max_heartCount = float('-inf')
    max_participant = None


    for row in reader:

        participant = row['Pnum']
        heartCount = float(row['HeartCount'])


        if heartCount > max_heartCount:
            max_heartCount = heartCount
            max_participant = participant

    print("Participant with maximum heartCount:", max_participant)
    print("Maximum heartCount:", max_heartCount)







