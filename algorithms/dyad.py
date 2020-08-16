from algorithms.session import Session
from algorithms.graph import match_graph_one_dyad, coordination_graph_one_dyad
from algorithms.params import POS_TAG
from statistics import mean
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
        for tr in tr_groups:
            session_name = str(self.dyad_num) + '_' + str(tr)
            s_df = self.df.loc[self.df[self.col['transcription']] == tr]
            key = s_df['transcription_hard_key'].iloc[0]
            sessions[key] = Session(s_df, key, self.attributes, self.speakers, session_name)
            session_num_key_dict[tr] = key
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

    def coordination_table(self, file_name):
        coor_val = self.get_coordination_dyad()
        index = coor_val._get_index_resolvers()['ilevel_0']
        dyad, session, t_key = [], [], []
        for i in index:
            d_s = i.split('_')
            dyad.append(d_s[0])
            session.append(d_s[1])
            t_key.append(self.session_key_dict[int(d_s[1])])
        coor_val.insert(column='dyad_n', value=dyad, loc=0)
        coor_val.insert(column='transcription_n', value=session, loc=1)
        coor_val.insert(column='transcription_hard_key', value=t_key, loc=2)
        if os.path.exists(file_name):
            coor_val.to_csv(file_name, mode='a')
        else:
            coor_val.to_csv(file_name)


    def lsm_table(self, writer):
        lsm_val = self.get_lsm_dyad()
        sessions_keys = key_to_arr(self.sessions)
        for i in range(len(lsm_val)):
            writer.writerow(self.lsm_row(sessions_keys[i], lsm_val.iloc[i]))

    def lsm_row(self, key, values):
        ans = [self.dyad_num, key]
        for v in values:
            ans.append(v)
        ans.append(mean(list(map(float, values))))
        return ans

    def get_target(self, speaker):
        first = self.speakers[0]
        return first if first is not speaker else self.speakers[1]

    def plot_lsm_graph(self, directory):
        match_graph_one_dyad(directory, self.get_lsm_dyad(), self.dyad_num)

    def plot_coordination_graph(self, directory):
        coordination_graph_one_dyad(directory, self.get_coordination_dyad(), self.dyad_num)


def key_to_arr(dict):
    return [key for key in dict]
