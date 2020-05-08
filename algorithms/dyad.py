from algorithms.session import Session
from algorithms import graph
from algorithms.params import POS_TAG
from statistics import mean

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
            s_df = self.df.loc[self.df[self.col['transcription']] == tr]
            key = s_df['transcription_hard_key'].iloc[0]
            sessions[key] = Session(s_df, key, self.attributes, self.speakers)
        return sessions

    def get_coordination_dyad(self):
        c_client_as_speaker, c_client_as_target = [], []
        for session in self.sessions.values():
            coordination = session.get_coordination()
            c_client_as_speaker.append(coordination[0])
            c_client_as_target.append(coordination[1])
        return c_client_as_speaker, c_client_as_target

    def get_lsm_dyad(self):
        return [session.get_LSM() for session in self.sessions.values()]

    def avg_lsm_score(self):
        matches = self.get_lsm_dyad()
        avg = []
        for m in matches:
            avg.append((m[0] + m[1]) / 2)
        return avg

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


def key_to_arr(dict):
    return [key for key in dict]
