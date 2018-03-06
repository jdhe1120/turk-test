import os
import pickle
import csv
import random

LOCATION = 'test_quiz'

lst = []

# read in data
for root, dirs, files in os.walk(LOCATION):
    for file in files:
        if file.endswith(".p"):
            data = pickle.load(open(root + '/' + file, "rb"))
            lst.append(data)

with open("trial1.csv", "w") as file:
    writer = csv.writer(file)
    features = ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"]

    writer.writerow(features + ["rec", "ans"])
    for datapoint in lst:
        feature_data = datapoint[0]
        feature_names = datapoint[1] 
        answer = int(datapoint[2][-1:])
        row = [None] * 5
        rec = random.randint(0, 1)
        ans = 'Yes' if (answer == rec) else 'No'
        for i in range(len(feature_data)):
            feature_num = int(feature_names[i][-1:])
            feature_val = feature_data[i]
            row[feature_num - 1] = feature_val
        writer.writerow(row + [rec, ans])