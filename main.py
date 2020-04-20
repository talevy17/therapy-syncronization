import pandas as pd
from dyad import Dyad
import csv
from graph import c_graphs, calc_all_dyad_graph


# origin data
def get_lsm(df, col):
    # list of all of the couples
    dyad_groups = df[col['dyad']].unique()
    lsm_val = {}
    for d in dyad_groups:
        dyad_obj = Dyad(d, col, df.loc[df[col['dyad']] == d])
        lsm_val[d] = dyad_obj.get_lsm_dyad()
    return lsm_val


def get_coor(df, col):
    dyad_groups = df[col['dyad']].unique()
    c_val = {}
    for d in dyad_groups:
        dyad_obj = Dyad(d, col, df.loc[df[col['dyad']] == d])
        c_val[d] = dyad_obj.get_coordination_dyad()
        break
    return c_val


def create_tables(df, col, file_name, att, lsm=False):
    dyad_groups = df[col['dyad']].unique()
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(att)
        for d in dyad_groups:
            dyad_obj = Dyad(d, col, df.loc[df[col['dyad']] == d])
            dyad_obj.tables(writer, lsm)


def add_table(df, params):
    coor_table_att = ['dyad_number', 'session_key', 'speaker', 'target'
                      'c_speaker:target_pos', 'c_speaker:target_neg', 'c_speaker:target_avg',
                      'c_target:speaker_pos', 'c_target:speaker_neg', 'c_target:speaker_avg']

    lsm_table_att = ['dyad_number', 'session_key', 'LSM_positive', 'LSM_negative']
    # create coor table
    create_tables(df, params, 'files/table_coordination.csv', coor_table_att)
    # create lsm table
    create_tables(df, params, 'files/table_lsm.csv', lsm_table_att, lsm=True)


def load_data(file_name):
    df = pd.read_csv(file_name)
    params = {'dyad': 'dyad_n',
              'transcription': 'transcription_n',
              'params': ['positive_v1', 'negative_v1'],
              'speakers': ['Client', 'Therapist'],
              'num_of_words': 'num_of_words'}
    # lsm_val = get_lsm(df, params)
    # t = get_coor(df, params)

    add_table(df, params)

    # calc_all_dyad_graph(t,['speaker', 'target'],3)


if __name__ == '__main__':
    load_data('files/MBM_camouflage_AllWithSBS.csv')
