NUM_OF_CHECK = 4

POS_TAG = ['adverb_pos_tag',
           'at_pos_tag',
           'cc_pos_tag',
           'conj_pos_tag',
           'cop_pos_tag',
           'def_pos_tag',
           'dt_pos_tag',
           'dtt_pos_tag',
           'ex_pos_tag',
           'in_pos_tag',
           'md_pos_tag',
           'pos_pos_tag',
           'preposition_pos_tag',
           'prp_pos_tag',
           'qw_pos_tag',
           'rb_pos_tag',
           'rel_pos_tag',
           's_prn_pos_tag',
           'temp_pos_tag']


def get_coor_table_att():
    att = ['dyad_number', 'session_key', 'speaker', 'target']
    s_t = ['c_speaker:target_{}'.format(pt) for pt in POS_TAG]
    t_s = ['c_target:speaker_{}'.format(pt) for pt in POS_TAG]
    return att + s_t + ['c_speaker:target_avg'] + t_s + ['c_target:speaker_avg']


pt_labels = ['adv', 'at', 'cc', 'conj', 'cop', 'def',
             'dt', 'dtt', 'ex', 'in', 'md', 'pos',
             'prep', 'prp', 'qw', 'rb', 'rel', 's_prn', 'tmp']
