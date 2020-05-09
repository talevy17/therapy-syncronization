import pandas as pd
from dyad import Dyad
import csv
from params import POS_TAG, get_coor_table_att, pt_labels
from graph import coor_all_dyad_graph


# origin data
def calc_lsm(df, col, plot_graph=False):
    # list of all of the couples
    dyad_groups = df[col['dyad']].unique()
    lsm_val = {}
    for d in dyad_groups:
        dyad_obj = Dyad(d, col, df.loc[df[col['dyad']] == d])
        lsm_val[d] = dyad_obj.get_lsm_dyad()
        if plot_graph:
            dyad_obj.plot_lsm_graph()
    return lsm_val


def calc_coordination(df, col, plot_graph=False):
    dyad_groups = df[col['dyad']].unique()
    c_val = {}
    for d in dyad_groups:
        dyad_obj = Dyad(d, col, df.loc[df[col['dyad']] == d])
        c_val[d] = dyad_obj.get_coordination_dyad()
        break
    if plot_graph:
        from params import POS_TAG
        coor_all_dyad_graph(c_val, ['speaker', 'target'], POS_TAG, pt_labels)
    return c_val


def create_tables(df, col, file_name, att, lsm=False):
    dyad_groups = df[col['dyad']].unique()
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(att)
        for d in dyad_groups:
            dyad_obj = Dyad(d, col, df.loc[df[col['dyad']] == d])
            dyad_obj.tables(writer, lsm)


def get_table(df, params):

    coor_table_att = get_coor_table_att()
    lsm_table_att = ['dyad_number', 'session_key'] + POS_TAG + ['lsm_avg']
    # create coor table
    create_tables(df, params, 'files/table_coordination.csv', coor_table_att)
    # create lsm table
    create_tables(df, params, 'files/table_lsm.csv', lsm_table_att, lsm=True)





def load_data(file_name):
    df = pd.read_csv(file_name)
    params = {'dyad': 'dyad_n',
              'transcription': 'transcription_n',
              'speakers': ['Client', 'Therapist'],
              'num_of_words': 'num_of_words'}
    # lsm_val = calc_lsm(df, params, plot_graph=True)
    t = calc_coordination(df, params, plot_graph=True)
    # get_table(df, params)
    # coor_all_dyad_graph(t,['speaker', 'target'],3)


if __name__ == '__main__':
    load_data('files/MBM_camouflage_AllWithSBS.csv')
