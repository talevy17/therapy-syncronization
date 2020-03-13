import pandas as pd
from dyad import dyad
import csv


# origin data
def get_lsm(df, col):
    # list of all of the couples
    dyad_groups = df[col['dyad']].unique()
    lsm_val = {}
    for d in dyad_groups:
        dyad_obj = dyad(d, col, df.loc[df[col['dyad']] == d])
        lsm_val[d] = dyad_obj.match_dyad()
    return lsm_val

def create_lsm_tables(df,col):
    dyad_groups = df[col['dyad']].unique()
    with open('files/table.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for d in dyad_groups:
            dyad_obj = dyad(d, col, df.loc[df[col['dyad']] == d])
            dyad_obj.tables(writer)

def load_data(file_name):
    df = pd.read_csv(file_name)
    params = {'dyad': 'dyad_n',
              'transcription': 'transcription_n',
              'params': ['positive_v1', 'negative_v1'],
              'speakers': ['Client', 'Therapist'],
              'num_of_words': 'num_of_words'}
    lsm_val = get_lsm(df, params)


def main():
    load_data('files/MBM_camouflage_AllWithSBS_Emo.csv')


if __name__ == '__main__':
    main()
