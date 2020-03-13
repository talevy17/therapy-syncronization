SPEAKER = 'event_speaker'
NUM_OF_WORDS = 'num_of_words'


class lsm:
    def __init__(self, params, speakers):
        self.params = params
        self.speakers = speakers

    '''
    preps1 - percent of pos/neg words for the first speaker
    preps1 - percent of pos/neg words for the second speaker
    add 0.0001 in case the denominator==0
    '''

    def calc_lsm(self, preps1, preps2):
        ans = 1 - (abs(preps1 - preps2) / (preps1 + preps2 + 0.0001))
        return "{0:.2f}".format(ans)
    # 
    def calc_percent_by_speaker(self, df, speaker):
        all_words = sum(df[NUM_OF_WORDS])
        speaker_data = df.loc[df[SPEAKER] == speaker]
        return [sum(speaker_data[p]) / all_words for p in self.params]

    # get filtered data
    def get_match(self, df):
        speakers_pos_neg = [(self.calc_percent_by_speaker(df, s)) for s in self.speakers]
        lsm_calcs = []  # LSM pos, LSM neg
        for i in range(len(self.params)):
            lsm_calcs.append(self.calc_lsm(speakers_pos_neg[0][i], speakers_pos_neg[1][i]))
        return lsm_calcs

