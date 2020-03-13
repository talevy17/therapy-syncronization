from lsm_calculator import lsm
import matplotlib.pyplot as plt


class dyad:
    def __init__(self, dyad_number, data_col, data):
        self.dyad_num = dyad_number
        self.col = data_col
        self.df = data
        # self.sessions = {}

    def match_dyad(self):
        tr_groups = self.df[self.col['transcription']].unique()
        lsm_val = lsm(self.col['params'], self.col['speakers'])
        match = []
        for tr in tr_groups:
            match.append(lsm_val.get_match(self.df.loc[self.df[self.col['transcription']] == tr]))
        return match

    def avg_lsm_score(self):
        matches = self.match_dyad()
        avg = []
        for m in matches:
            avg.append((m[0] + m[1]) / 2)
        return avg

    def tables(self, writer):
        m = self.match_dyad()
        writer.writerow(['dyad number : ' + str(self.dyad_num)])
        writer.writerow(['session number', 'LSM positive', 'LSM negative'])
        for i in range(len(m)):
            writer.writerow([i, m[i][0], m[i][1]])

    def avg_graph(self):
        avg_val = self.avg_lsm_score()
        plt.plot(avg_val)
        plt.xlabel('session number')
        plt.ylabel('LSM avg')
        plt.title('Positive and negative avg over sessions')
        plt.savefig(str(self.dyad_num))
        plt.show()

    def match_graph(self):
        match_along_sessions = self.match_dyad()
        plt.plot(match_along_sessions)
        plt.xlabel('session number')
        plt.ylabel('LSM')
        plt.title('Positive and negative matching over sessions')
        plt.savefig(str(self.dyad_num))
        plt.show()

# TODO - well, maybe in the future

# class session:
#     def __init__(self, dyad_number, session_number, data_col, data):
#         self.dyad_num = dyad_number
#         self.col = data_col
#         self.df = data
#         self.transcription = session_number
#         self.num_of_words = data['num_of_words']
#         self.lsm = []
