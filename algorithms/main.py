import pandas as pd
from dyad import Dyad
import csv
from params import POS_TAG, get_coor_table_att, pt_labels
from graph import coor_all_dyad_graph

TMP_PARAMS = {'dyad': 'dyad_n',
              'transcription': 'transcription_n',
              'speakers': ['Client', 'Therapist'],
              'num_of_words': 'num_of_words'}


# origin data
def plot_lsm(df, col):
    # list of all of the couples
    dyad_groups = df[col['dyad']].unique()
    for d in dyad_groups:
        dyad_obj = Dyad(d, col, df.loc[df[col['dyad']] == d])
        dyad_obj.plot_lsm_graph()


def plot_coordination(df, col, plot_graph=False):
    dyad_groups = df[col['dyad']].unique()
    c_val = {}
    for d in dyad_groups:
        dyad_obj = Dyad(d, col, df.loc[df[col['dyad']] == d])
        c_val[d] = dyad_obj.get_coordination_dyad()
    if plot_graph:
        from params import POS_TAG
        coor_all_dyad_graph(c_val, ['speaker', 'target'], POS_TAG, pt_labels)


def create_tables(df, col, file_name, att, lsm=False):
    dyad_groups = df[col['dyad']].unique()
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(att)
        for d in dyad_groups:
            dyad_obj = Dyad(d, col, df.loc[df[col['dyad']] == d])
            dyad_obj.tables(writer, lsm)


def get_table(df, params, lsm):
    if lsm:
        lsm_table_att = ['dyad_number', 'session_key'] + POS_TAG + ['lsm_avg']
        create_tables(df, params, 'files/lsm_table.csv', lsm_table_att, lsm=True)
    else:
        coor_table_att = get_coor_table_att()
        create_tables(df, params, 'files/coordination_table.csv', coor_table_att)


def zip_graph(df, params, lsm):
    if lsm:
        plot_lsm(df, params)
    else:
        plot_coordination(df, params)


def controller(file_name, params, table=False, graphs=False, lsm=False):
    df = pd.read_csv('files/' + file_name)
    if table:
        get_table(df, params, lsm)
    if graphs:
        zip_graph(df, params, lsm)


if __name__ == '__main__':
    controller('files/MBM_camouflage_AllWithSBS.csv', TMP_PARAMS)
