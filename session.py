class session:
    def __init__(self, df):
        self.df = df
        self.props = {}

    @staticmethod
    def compute_by_tag(speaker, target, tag):
        return (speaker[tag]['con'] / target[tag]) - speaker[tag]['gen']

    def calc_prob(self, speaker, target):
        return [self.compute_by_tag(speaker, target, 'pos'), self.compute_by_tag(speaker, target, 'neg')]

    def get_prob_by_speaker(self, speaker, target, threshold):
        if self.props[speaker]:
            return self.props[speaker]
        general_speaker = {}
        general_target = {}
        speaker_data = self.df.loc[self.df['event_speaker'] == speaker]
        target_data = self.df.loc[self.df['event_speaker'] == target]
        general_speaker['pos'] = self.df.loc[self.df['event_speaker'] == speaker]