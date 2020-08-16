import matplotlib.pyplot as plt
import os
from algorithms.params import speakers


def set_x_ax(df, dyad_num):
    suffix = str(dyad_num) + '_'
    df = df.rename(index=lambda s: s.replace(suffix, ''))
    return df


'''
coordination graph
'''


def filter_graph(df, speaker_to_target, speaker, filter_avg=False):
    df = df.loc[(df['s:t'] == speaker_to_target) & (df['speaker'] == speaker)]
    if filter_avg:
        df = df.filter(items=['avg'])
    return df


def coordination_graph_one_dyad(directory, coordination_dyad, dyad_num):
    df = set_x_ax(coordination_dyad, dyad_num)
    # fixme - hard coded
    speaker_to_target = ['0','1']
    color = ['#6FBBA3', '#6F91BB']
    titles= ['Speaker Coordination', 'Target Coordination']
    for i in range(len(speaker_to_target)):
        for speaker in speakers:
            plt.switch_backend('Agg')
            graph_to_plot = filter_graph(df, speaker_to_target[i], speaker, filter_avg=True)
            graph_to_plot.plot.bar(y='avg', color=color[i])
            plt.ylabel('coordination: speaker='+speaker)
            plt.xlabel('session')
            plt.title(titles[i])
            if not os.path.exists(directory):
                os.makedirs(directory)
            plt.savefig(os.path.join(directory, str(dyad_num)+'_s: '+speaker))
            plt.close()

'''
lsm graphs
'''


def match_graph_one_dyad(directory, match_along_sessions, dyad_num):
    df = match_along_sessions['avg']
    df = set_x_ax(df, dyad_num)
    plt.switch_backend('Agg')
    df.plot(kind='line', color='#0F5762')
    plt.xlabel('session number')
    plt.ylabel('pos-tag LSM average')
    plt.title('LSM over sessions')
    plt.grid(True, color='#E8E8E9')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.savefig(os.path.join(directory, str(dyad_num)))
    plt.close()
