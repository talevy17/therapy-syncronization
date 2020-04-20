from session import Session

class Dyad:
    def __init__(self, dyad_number, data_col, data):
        self.dyad_num = dyad_number
        self.col = data_col
        self.df = data
        self.attributes = ['positive_v1', 'negative_v1']
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

    # add key
    def tables(self, writer):
        m = self.get_lsm_dyad()
        sessions_keys = key_to_arr(self.sessions)
        for i in range(len(m)):
            writer.writerow(self.row(sessions_keys[i], m[i]))

    def row(self, key, values):
        ans =[self.dyad_num, key]
        for v in values:
            ans.append(v)
        return ans

def key_to_arr(dict):
    return [key for key in dict]
