from algorithms.session import Session
from algorithms.graph import match_graph_one_dyad, coordination_graph_one_dyad
from algorithms.params import POS_TAG
from statistics import mean
import pandas as pd


class Dyad:
    def __init__(self, dyad_number, data_col, data):
        self.dyad_num = dyad_number
        self.col = data_col
        self.df = data
        self.attributes = POS_TAG
        self.speakers = ['Client', 'Therapist']
        self.sessions = self.split_sessions()

    def split_sessions(self):
        tr_groups = self.df[self.col['transcription']].unique()
        # transcription_hard_key : session
        sessions = {}
        for tr in tr_groups:
            session_name = str(self.dyad_num) + '_' + str(tr)
            s_df = self.df.loc[self.df[self.col['transcription']] == tr]
            key = s_df['transcription_hard_key'].iloc[0]
            sessions[key] = Session(s_df, key, self.attributes, self.speakers, session_name)
        return sessions

    def get_coordination_dyad(self):
        coordination_by_dyad_df = pd.DataFrame()
        for session in self.sessions.values():
            coordination_by_dyad_df = coordination_by_dyad_df.append(session.get_coordination())
        return coordination_by_dyad_df

    def get_lsm_dyad(self):
        lst = [session.get_LSM() for session in self.sessions.values()]
        index_name = [str(self.dyad_num)+'_'+str(i) for i in range(len(lst))]
        col = POS_TAG+['avg']
        lsm_df = pd.DataFrame(lst, columns=col, index=index_name)
        return lsm_df

    def tables(self, writer, lsm):
        self.lsm_table(writer) if lsm else self.coordination_table(writer)

    def coordination_table(self, writer):
        coor_val = self.get_coordination_dyad()
        sessions_keys = key_to_arr(self.sessions)
        for speaker in range(len(coor_val)):
            for i in range(len(coor_val[speaker])):
                writer.writerow(self.coor_row(sessions_keys[i],
                                              self.speakers[speaker],
                                              coor_val[speaker][i]))

    def lsm_table(self, writer):
        lsm_val = self.get_lsm_dyad()
        sessions_keys = key_to_arr(self.sessions)
        for i in range(len(lsm_val)):
            writer.writerow(self.lsm_row(sessions_keys[i], lsm_val[i]))

    def lsm_row(self, key, values):
        ans = [self.dyad_num, key]
        for v in values:
            ans.append(v)
        ans.append(mean(list(map(float, values))))
        return ans

    def coor_row(self, key, speaker, values):
        ans = [self.dyad_num, key, speaker, self.get_target(speaker)]
        for tuple in values:
            for arg in tuple.values():
                ans.append(arg)
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
