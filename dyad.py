from lsm_calculator import LSM
from session import Session


class Dyad:
    def __init__(self, dyad_number, data_col, data):
        self.dyad_num = dyad_number
        self.col = data_col
        self.df = data

    def get_coordination_dyad(self):
        tr_groups = self.df[self.col['transcription']].unique()
        c_client_as_speaker = []
        c_client_as_target = []
        for tr in tr_groups:
            s = Session(self.df.loc[self.df[self.col['transcription']] == tr])
            attributes = ['positive_v1', 'negative_v1']
            c_client_as_speaker.append(s.get_coor_by_speaker('Client', 'Therapist', attributes, threshold=1))
            c_client_as_target.append(s.get_coor_by_speaker('Therapist', 'Client', attributes, threshold=1))
        return c_client_as_speaker, c_client_as_target

    def get_lsm_dyad(self):
        tr_groups = self.df[self.col['transcription']].unique()
        lsm_val = LSM(self.col['params'], self.col['speakers'])
        match = []
        for tr in tr_groups:
            match.append(lsm_val.get_match(self.df.loc[self.df[self.col['transcription']] == tr]))
        return match

    def avg_lsm_score(self):
        matches = self.get_lsm_dyad()
        avg = []
        for m in matches:
            avg.append((m[0] + m[1]) / 2)
        return avg

    def tables(self, writer):
        m = self.get_lsm_dyad()
        writer.writerow(['dyad number : ' + str(self.dyad_num)])
        writer.writerow(['session number', 'LSM positive', 'LSM negative'])
        for i in range(len(m)):
            writer.writerow([i, m[i][0], m[i][1]])

