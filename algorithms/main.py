import os
import zipfile
import pandas as pd
from algorithms.dyad import Dyad
import csv
from algorithms.params import POS_TAG, get_coor_table_att, pt_labels
from algorithms.graph import coor_all_dyad_graph

TMP_PARAMS = {'dyad': 'dyad_n',
              'transcription': 'transcription_n',
              'speakers': ['Client', 'Therapist'],
              'num_of_words': 'num_of_words'}


# origin data
def plot_lsm(df, col, directory):
    # list of all of the couples
    dyad_groups = df[col['dyad']].unique()
    for d in dyad_groups:
        dyad_obj = Dyad(d, col, df.loc[df[col['dyad']] == d])
        dyad_obj.plot_lsm_graph(directory)


def plot_coordination(df, col, directory):
    dyad_groups = df[col['dyad']].unique()
    c_val = {}
    for d in dyad_groups:
        dyad_obj = Dyad(d, col, df.loc[df[col['dyad']] == d])
        c_val[d] = dyad_obj.get_coordination_dyad()
    coor_all_dyad_graph(c_val, ['speaker', 'target'], POS_TAG, pt_labels, directory)


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
        return 'lsm_table.csv'
    else:
        coor_table_att = get_coor_table_att()
        create_tables(df, params, 'files/coordination_table.csv', coor_table_att)
        return 'coordination_table.csv'


def create_zip_file(zip_file_name, zip_path):
    zip_file = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
    compress(zip_path, zip_file)
    zip_file.close()


def compress(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def zip_graph(df, params, lsm):
    if lsm:
        directory = os.path.abspath('../files/lsm_graphs/')
        plot_lsm(df, params, directory)
        create_zip_file('../files/lsm_graphs.zip', '../files/lsm_graphs')
        return 'lsm_graphs.zip'
    else:
        directory = os.path.abspath('../files/coordination_graphs/')
        plot_coordination(df, params, directory)
        create_zip_file('../files/coordination_graphs.zip', '../files/coordination_graphs')
        return 'coordination_graphs.zip'


def controller(file_name, params=None, table=False, graphs=False, lsm=False):
    if not params:
        params = TMP_PARAMS
    df = pd.read_csv('../files/' + file_name)
    if table:
        return get_table(df, params, lsm)
    if graphs:
        return zip_graph(df, params, lsm)


if __name__ == '__main__':
    print(controller('MBM_camouflage_AllWithSBS.csv', TMP_PARAMS, lsm=False, graphs=True))
