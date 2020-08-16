import os
import zipfile
import pandas as pd
from algorithms.dyad import Dyad
from algorithms.params import POS_TAG, get_coor_table_att


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
    for d in dyad_groups:
        dyad_obj = Dyad(d, col, df.loc[df[col['dyad']] == d])
        dyad_obj.plot_coordination_graph(directory)


def create_tables(df, col, file_name, att, lsm=False):
    dyad_groups = df[col['dyad']].unique()
    for d in dyad_groups:
        dyad_obj = Dyad(d, col, df.loc[df[col['dyad']] == d])
        dyad_obj.tables(file_name, lsm)


def get_table(df, params, measures,lsm):
    if lsm:
        file_name = 'lsm_table.csv'
        lsm_table_att = ['dyad_number', 'session_key'] + measures + ['lsm_avg']
        create_tables(df, params, 'files/' + file_name, lsm_table_att, lsm=True)
        return file_name
    else:
        file_name = 'coordination_table.csv'
        coor_table_att = get_coor_table_att()
        create_tables(df, params, 'files/' + file_name, coor_table_att)
        return file_name


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
        file_name = 'lsm_graphs'
        directory = os.path.abspath('files/' + file_name + '/')
        plot_lsm(df, params, directory)
        create_zip_file('files/' + file_name + '.zip', 'files/' + file_name)
        return file_name + '.zip'
    else:
        file_name = 'coordination_graphs'
        directory = os.path.abspath('files/' + file_name + '/')
        plot_coordination(df, params, directory)
        create_zip_file('files/' + file_name + '.zip', 'files/' + file_name)
        return file_name + '.zip'


def controller(file_name, params=None, measures=None, table=False, graphs=False, lsm=False):
    if not params:
        params = TMP_PARAMS
    if not measures:
        measures = POS_TAG
    df = pd.read_csv('files/' + file_name)
    if table:
        return get_table(df, params, measures, lsm)
    if graphs:
        return zip_graph(df, params, lsm)


if __name__ == '__main__':
    controller('MBM_camouflage_AllWithSBS.csv', params=TMP_PARAMS, measures=POS_TAG,
               table=True, graphs=False, lsm=False)