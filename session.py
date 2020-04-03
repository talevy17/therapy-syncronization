from statistics import mean
PERSON = 'event_speaker'
TURN = 'dialog_turn_main_speaker'


class Session:
    def __init__(self, df):
        self.df = df
        self.speaker_to_target = {}
        self.target_to_speaker = {}

    def get_coor_by_speaker(self, speaker, target, attributes, threshold=1):
        if speaker in self.speaker_to_target and target in self.target_to_speaker:
            return self.speaker_to_target[speaker], self.target_to_speaker[target]
        general_speaker, general_target, tagged_exchanges, speaker_tag, target_tag = self.init_dictionaries()
        curr = target
        start = True
        total_exchanges = 0
        for _, row in self.df.iterrows():
            if start:
                if not row[TURN] == target:
                    continue
                else:
                    start = False
            if not row[TURN] == row[PERSON]:
                continue
            prev = curr
            curr = row[TURN]
            if prev != curr:
                if curr == target:
                    speaker_tag, target_tag, general_target, general_speaker =\
                        self.exchange_handler(threshold, attributes, speaker_tag,
                                              target_tag, general_target, general_speaker)
                else:
                    tagged_exchanges += 1
            if curr == target:
                for tag in attributes:
                    target_tag[tag] += row[tag]
            else:
                for tag in attributes:
                    speaker_tag[tag] += row[tag]
        self.get_probs_by_tags(attributes, speaker,
                               target, total_exchanges, general_target, general_speaker, tagged_exchanges)
        return self.speaker_to_target[speaker], self.target_to_speaker[target]

    def add_avg_to_dict(self, speaker, target):
        self.speaker_to_target[speaker]['avg'] = mean(list(self.speaker_to_target[speaker].values()))
        self.target_to_speaker[target]['avg'] = mean(list(self.target_to_speaker[target].values()))

    def get_probs_by_tags(self, attributes, speaker, target, total_exchanges,
                          general_target, general_speaker, tagged_exchanges):
        for tag in attributes:
            if speaker not in self.speaker_to_target:
                self.speaker_to_target[speaker] = {}
            if target not in self.target_to_speaker:
                self.target_to_speaker[target] = {}
            if total_exchanges > 0:
                general_target[tag] /= total_exchanges
                general_speaker[tag] /= total_exchanges
                conditioned = tagged_exchanges[tag] / total_exchanges
                self.speaker_to_target[speaker][tag] = (conditioned / (general_target[tag] + 0.001)) - general_speaker[tag]
                self.target_to_speaker[target][tag] = (conditioned / (general_speaker[tag] + 0.001)) - general_target[tag]
            else:
                self.speaker_to_target[speaker][tag] = 0
                self.target_to_speaker[target][tag] = 0
        self.add_avg_to_dict(speaker, target)

    @staticmethod
    def init_dictionaries():
        general_speaker = {tag: 0 for tag in attributes}
        general_target = {tag: 0 for tag in attributes}
        tagged_exchanges = {tag: 0 for tag in attributes}
        speaker_tag = {tag: 0 for tag in attributes}
        target_tag = {tag: 0 for tag in attributes}
        return general_speaker, general_target, tagged_exchanges, speaker_tag, target_tag

    @staticmethod
    def exchange_handler(threshold, attributes, speaker_tag, target_tag, general_target, general_speaker):
        for tag in attributes:
            if speaker_tag[tag] >= threshold and target_tag[tag] >= threshold:
                tagged_exchanges[tag] += 1
            if target_tag[tag] >= threshold:
                general_target[tag] += 1
            if speaker_tag[tag] >= threshold:
                general_speaker[tag] += 1
            speaker_tag[tag] = target_tag[tag] = 0
        return speaker_tag, target_tag, general_target, general_speaker
