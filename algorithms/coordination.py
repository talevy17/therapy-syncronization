from statistics import mean
import pandas as pd
from params import POS_TAG

PERSON = 'event_speaker'
TURN = 'dialog_turn_main_speaker'
col = ['s:t', 't:s', 'speaker', 'target'] + POS_TAG + ['avg']


class Coordination:
    def __init__(self, df):
        self.df = df
        self.coorination_df = pd.DataFrame(columns=col)

    def get_coor_by_speaker(self, speaker, target, attributes, threshold=1):
        general_speaker, general_target, tagged_exchanges, speaker_tag, target_tag = self.init_dictionaries(attributes)
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
                    speaker_tag, target_tag, general_target, general_speaker, tagged_exchanges = \
                        self.exchange_handler(threshold, attributes, speaker_tag, target_tag, general_target,
                                              general_speaker,
                                              tagged_exchanges)
                else:
                    total_exchanges += 1
            if curr == target:
                for tag in attributes:
                    target_tag[tag] += row[tag]
            else:
                for tag in attributes:
                    speaker_tag[tag] += row[tag]
        self.get_probs_by_tags(attributes, speaker,
                               target, total_exchanges, general_target, general_speaker, tagged_exchanges)
        return self.coorination_df

    def add_avg(self, speaker, target):
        speaker['avg'] = mean(list(speaker.values()))
        target['avg'] = mean(list(target.values()))

    def get_probs_by_tags(self, attributes, speaker, target, total_exchanges,
                          general_target, general_speaker, tagged_exchanges):
        speaker_to_target = {}
        target_to_speaker = {}
        for tag in attributes:
            if total_exchanges > 0:
                general_target[tag] /= total_exchanges
                general_speaker[tag] /= total_exchanges
                conditioned = tagged_exchanges[tag] / total_exchanges
                speaker_to_target[tag] = (conditioned / (general_target[tag] + 0.001)) - general_speaker[tag]
                target_to_speaker[tag] = (conditioned / (general_speaker[tag] + 0.001)) - general_target[tag]
            else:
                speaker_to_target[tag] = 0
                target_to_speaker[tag] = 0
        self.add_avg(speaker_to_target, target_to_speaker)
        self.add_prbs_to_df(speaker_to_target, target_to_speaker, speaker, target)

    def add_prbs_to_df(self, speaker_to_target, target_to_speaker, speaker, target):
        speaker_to_target.update({'s:t': '1', 't:s': '0', 'speaker': speaker, 'target': target})
        target_to_speaker.update({'s:t': '0', 't:s': '1', 'speaker': target, 'target': speaker})
        self.coorination_df=self.coorination_df.append(speaker_to_target, ignore_index=True)
        self.coorination_df=self.coorination_df.append(target_to_speaker, ignore_index=True)

    @staticmethod
    def init_dictionaries(attributes):
        general_speaker = {tag: 0 for tag in attributes}
        general_target = {tag: 0 for tag in attributes}
        tagged_exchanges = {tag: 0 for tag in attributes}
        speaker_tag = {tag: 0 for tag in attributes}
        target_tag = {tag: 0 for tag in attributes}
        return general_speaker, general_target, tagged_exchanges, speaker_tag, target_tag

    @staticmethod
    def exchange_handler(threshold, attributes, speaker_tag, target_tag, general_target, general_speaker,
                         tagged_exchanges):
        for tag in attributes:
            if speaker_tag[tag] >= threshold and target_tag[tag] >= threshold:
                tagged_exchanges[tag] += 1
            if target_tag[tag] >= threshold:
                general_target[tag] += 1
            if speaker_tag[tag] >= threshold:
                general_speaker[tag] += 1
            speaker_tag[tag] = target_tag[tag] = 0
        return speaker_tag, target_tag, general_target, general_speaker, tagged_exchanges
