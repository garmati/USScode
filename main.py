import csv

# Open the CSV file
with open('circledata.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    # Initialize variables to store the maximum heartCount and corresponding participant ID
    max_heartCount = float('-inf')
    max_participant = None

    # Iterate over each row in the CSV
    for row in reader:
        # Extract the participant ID and heartCount values
        participant = row['Pnum']
        heartCount = float(row['HeartCount'])

        # Update the maximum heartCount and participant if the current value is greater
        if heartCount > max_heartCount:
            max_heartCount = heartCount
            max_participant = participant

    # Print the participant with the maximum heartCount
    print("Participant with maximum heartCount:", max_participant)
    print("Maximum heartCount:", max_heartCount)







