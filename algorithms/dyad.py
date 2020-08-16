from algorithms.session import Session
from algorithms.graph import match_graph_one_dyad, coordination_graph_one_dyad
from algorithms.params import POS_TAG
import pandas as pd
import os


class Dyad:
    def __init__(self, dyad_number, data_col, data):
        self.dyad_num = dyad_number
        self.col = data_col
        self.df = data
        self.attributes = POS_TAG
        self.speakers = ['Client', 'Therapist']
        self.sessions, self.session_key_dict = self.split_sessions()

    def split_sessions(self):
        tr_groups = self.df[self.col['transcription']].unique()
        # transcription_hard_key : session
        sessions = {}
        session_num_key_dict = {}
        for tr in range(len(tr_groups)):
            session_name = str(self.dyad_num) + '_' + str(tr)
            s_df = self.df.loc[self.df[self.col['transcription']] == tr_groups[tr]]
            key = s_df['transcription_hard_key'].iloc[0]
            sessions[key] = Session(s_df, key, self.attributes, self.speakers, session_name)
            session_num_key_dict[tr_groups[tr]] = key
        return sessions, session_num_key_dict

    def get_coordination_dyad(self):
        coordination_by_dyad_df = pd.DataFrame()
        for session in self.sessions.values():
            coordination_by_dyad_df = coordination_by_dyad_df.append(session.get_coordination())
        return coordination_by_dyad_df

    def get_lsm_dyad(self):
        lst = [session.get_LSM() for session in self.sessions.values()]
        index_name = [str(self.dyad_num) + '_' + str(i) for i in range(len(lst))]
        col = POS_TAG + ['avg']
        lsm_df = pd.DataFrame(lst, columns=col, index=index_name)
        return lsm_df

    def tables(self, writer, lsm):
        self.lsm_table(writer) if lsm else self.coordination_table(writer)

    def split_index(self, index, get_key=True):
        dyad, session, t_key = [], [], []
        for i in index:
            d_s = i.split('_')
            dyad.append(d_s[0])
            session.append(d_s[1])
            if get_key:
                t_key.append(self.session_key_dict[int(d_s[1])])
        if get_key:
            return dyad, session, t_key
        return dyad, session

    def add_dyad_info_col(self, df, dyad, session, t_key=None):
        df.insert(column='dyad_n', value=dyad, loc=0)
        df.insert(column='transcription_n', value=session, loc=1)
        if t_key:
            df.insert(column='transcription_hard_key', value=t_key, loc=2)
        return df

    def coordination_table(self, file_name):
        coor_val = self.get_coordination_dyad()
        index = coor_val._get_index_resolvers()['ilevel_0']
        dyad, session, t_key = self.split_index(index)
        self.add_dyad_info_col(coor_val, dyad, session, t_key)
        if os.path.exists(file_name):
            coor_val.to_csv(file_name, mode='a', index=False, header=False)
        else:
            coor_val.to_csv(file_name, index=False)

    def lsm_table(self, file_name):
        lsm_val = self.get_lsm_dyad()
        sessions_keys = key_to_arr(self.sessions)
        index = lsm_val._get_index_resolvers()['ilevel_0']
        dyad, session = self.split_index(index, get_key=False)
        self.add_dyad_info_col(lsm_val, dyad, session)
        lsm_val.insert(column='transcription_hard_key', value=sessions_keys, loc=2)
        if os.path.exists(file_name):
            lsm_val.to_csv(file_name, mode='a', index=False, header=False)
        else:
            lsm_val.to_csv(file_name, index=False)

    def plot_lsm_graph(self, directory):
        match_graph_one_dyad(directory, self.get_lsm_dyad(), self.dyad_num)

    def plot_coordination_graph(self, directory):
        coordination_graph_one_dyad(directory, self.get_coordination_dyad(), self.dyad_num)


def key_to_arr(dict):
    return [key for key in dict]
