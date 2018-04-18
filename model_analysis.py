import csv
import os
import numpy as np
import pandas as pd
import datetime as dt

datasets = ['past_iterations/human_data_04_18_2018/']
dir_path = os.path.dirname(os.path.realpath(__file__))

for data in datasets:
    csvfiles = []
    for _, _, files in os.walk(data):
        for fl in files:
            if fl.endswith(".csv"):
                csvfiles.append(fl)

    times = []
    accuracies = []

    count = 0
    for csvfile in csvfiles:
        fl = dir_path + '/' + data + '/' + csvfile
        df = pd.read_csv(fl)

        df2 = None
        df2 = df.loc[df.trial_type == 'survey-multi-choice'].reset_index(drop=True)

        df2 = df2.iloc[-13:].reset_index(drop=True)

        ids = []
        for ele in df2['question_id']:
            if np.isnan(ele):
                ids.append(-1)
            else:
                ids.append(int(str(ele).split('.')[1]))
        df2['question_id'] = ids

        times.append(df2['rt']/1000.)
        accuracies.append(df2['correct'])

        #df2 = df2.sort_values('question_id')

        #df2['correct'] = df2['correct'].astype(float)

        #practice = df2.head(n = 3)
        #experiment = df2[3:]

        #if sum(practice['correct']) >= 2:
        #    times.append(experiment['rt']/1000)
        #    accuracies.append(experiment['correct'])
        #else:
        #    print( "Excluded by practice" )

    today = dt.datetime.today().strftime('%m_%d_%Y')
    np.savetxt("analyzed/"+today + '_times.csv', times, delimiter = ',', fmt = '%s')
    np.savetxt("analyzed/"+today + '_accuracies.csv', accuracies, delimiter = ',', fmt = '%s')



