PERSON = 'event_speaker'
from statistics import mean

class Session:
    def __init__(self, df):
        self.df = df
        self.speaker_to_target = {}
        self.target_to_speaker = {}

    def get_coor_by_speaker(self, speaker, target, attributes, threshold=1):
        if speaker in self.speaker_to_target and target in self.target_to_speaker:
            return self.speaker_to_target[speaker], self.target_to_speaker[target]
        for tag in attributes:
            general_speaker = general_target = 0
            total_exchanges = tagged_exchanges = 0
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
                        if speaker_tag >= threshold and target_tag >= threshold:
                            tagged_exchanges += 1
                        if target_tag >= threshold:
                            general_target += 1
                        if speaker_tag >= threshold:
                            general_speaker += 1
                        speaker_tag = target_tag = 0
                    else:
                        total_exchanges += 1
                if curr == target:
                    target_tag += row[tag]
                else:
                    speaker_tag += row[tag]
            if speaker not in self.speaker_to_target:
                self.speaker_to_target[speaker] = {}
            if target not in self.target_to_speaker:
                self.target_to_speaker[target] = {}
            if total_exchanges > 0:
                general_target /= total_exchanges
                general_speaker /= total_exchanges
                conditioned = tagged_exchanges / total_exchanges
                self.speaker_to_target[speaker][tag] = (conditioned / (general_target + 0.001)) - general_speaker
                self.target_to_speaker[target][tag] = (conditioned / (general_speaker + 0.001)) - general_target
            else:
                self.speaker_to_target[speaker][tag] = 0
                self.target_to_speaker[target][tag] = 0
        self.add_avg_to_dict(speaker, target)
        return self.speaker_to_target[speaker], self.target_to_speaker[target]

    def add_avg_to_dict(self, speaker, target):
        self.speaker_to_target[speaker]['avg'] = mean(list(self.speaker_to_target[speaker].values()))
        self.target_to_speaker[target]['avg'] = mean(list(self.target_to_speaker[target].values()))
