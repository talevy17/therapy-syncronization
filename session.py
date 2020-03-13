PERSON = 'event_speaker'


class Session:
    def __init__(self, df):
        self.df = df
        self.probs = {}

    @staticmethod
    def get_gen_prob_by_tag(data, tag, threshold):
        return len(data.loc[data[tag] > threshold]) / len(data)

    def get_prob_by_speaker(self, speaker, target, attributes, threshold=1):
        if self.probs[speaker]:
            return self.probs[speaker]
        speaker_data = self.df.loc[self.df[PERSON] == speaker]
        target_data = self.df.loc[self.df[PERSON] == target]
        for tag in attributes:
            general_speaker = self.get_gen_prob_by_tag(speaker_data, tag, threshold)
            general_target = self.get_gen_prob_by_tag(target_data, tag, threshold)
            total_exchanges = 0
            tagged_exchanges = 0
            curr = prev = target
            start = True
            speaker_tag = target_tag = 0
            for _, row in self.df.iterrows():
                if start:
                    if not row[PERSON] == target:
                        continue
                    else:
                        start = False
                prev = curr
                curr = row[PERSON]
                if prev != curr:
                    if curr == target:
                        if speaker_tag > threshold and target_tag > threshold:
                            tagged_exchanges += 1
                        speaker_tag = target_tag = 0
                    else:
                        total_exchanges += 1
                if curr == target:
                    target_tag += row[tag]
                else:
                    speaker_tag += row[tag]
            conditioned = tagged_exchanges / total_exchanges
            self.probs[speaker][tag] = (conditioned / general_target) - general_speaker
        return self.probs[speaker]
