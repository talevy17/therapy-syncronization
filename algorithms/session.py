from algorithms.coordination import Coordination
from algorithms.lsm_calculator import LSM
import pandas as pd
from params import NUM_OF_CHECK

class Session:
    def __init__(self, df, id, attributes, speakers, session_name):
        self.df = df
        self.id = id
        self.attributes = attributes
        self.speakers = speakers
        self.session_name = session_name

    def get_coordination(self):
        c = Coordination(self.df)
        c.get_coor_by_speaker(self.speakers[0], self.speakers[1], self.attributes, threshold=1)
        speakers_df = c.get_coor_by_speaker(self.speakers[1], self.speakers[0], self.attributes, threshold=1)
        session_coordination_df = pd.DataFrame(speakers_df)
        session_coordination_df.rename(index={i:self.session_name for i in range(NUM_OF_CHECK)}, inplace=True)
        return session_coordination_df


    def get_LSM(self):
        lsm_val = LSM(self.attributes, self.speakers, self.df)
        return lsm_val.get_match()
