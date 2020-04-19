from coordination import Coordination
from lsm_calculator import LSM


class Session:
    def __init__(self, df, id, attributes, speakers):
        self.df = df
        self.id = id
        self.attributes = attributes
        self.speakers = speakers

    def get_coordination(self):
        c = Coordination(self.df)
        return c.get_coor_by_speaker(self.speakers[0], self.speakers[1], self.attributes, threshold=1), \
               c.get_coor_by_speaker(self.speakers[1], self.speakers[0], self.attributes, threshold=1)

    def get_LSM(self):
        lsm_val = LSM(self.attributes, self.speakers, self.df)
        return lsm_val.get_match()
