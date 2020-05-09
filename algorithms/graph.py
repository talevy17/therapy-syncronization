from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import softmax
import os


def split_data_to_graph(data, speakers):
    first_graph = {i: [] for i in speakers}
    second_graph = {i: [] for i in speakers}
    for s in range(len(data[0])):
        for i in range(len(speakers)):
            first_graph[speakers[i]].append(softmax(list(data[i][s][0].values())))
            second_graph[speakers[i]].append(softmax(list(data[i][s][1].values())))
    params = len(first_graph[speakers[0]][0])
    return add_avg(first_graph, speakers, params), add_avg(second_graph, speakers, params)


def add_avg(data, speakers, params_n):
    d = {i: [] for i in speakers}
    for s in speakers:
        for c in range(params_n):
            d[s].append(mean(list(data[s][session][c] for session in range(len(data[s])))))
    return d


def c_graphs(coor_all_dyad):
    dyad_dict = {}
    for d in coor_all_dyad:
        dyad_dict[d] = split_data_to_graph(coor_all_dyad[d], ['speaker', 'target'])
    return dyad_dict


def merge_data(coor_all_dyad, speakers, att):
    data = c_graphs(coor_all_dyad)
    first_graph = {}
    second_graph = {}
    for s in speakers:
        first_graph[s] = [mean(list(data[d][0][s][a]
                                    for d in range(len(data)))) for a in range(len(att))]
        second_graph[s] = [mean(list(data[d][1][s][a]
                                     for d in range(len(data)))) for a in range(len(att))]
    return first_graph, second_graph


def coor_all_dyad_graph(coor_all_dyad, speakers, att, att_labels, directory):
    first_g, sec_g = merge_data(coor_all_dyad, speakers, att)
    plot_graph(directory, [first_g['speaker'], first_g['target']],
               ['speaker: therapist', 'speaker: client'], 's',
               'Speaker Coordination', att_labels)
    plot_graph(directory, [sec_g['speaker'], sec_g['target']],
               ['target: therapist', 'target: client'], 't',
               'Target Coordination', att_labels)


def plot_graph(directory, data_bars, labels, name, title, att):
    fig, ax = plt.subplots()
    index = np.arange(len(att))
    bar_width = 0.2
    opacity = 0.3
    rects1 = plt.bar(index, data_bars[0], bar_width,
                     alpha=opacity,
                     color='b',
                     label=labels[0])
    rects2 = plt.bar(index + bar_width, data_bars[1], bar_width,
                     alpha=opacity,
                     color='g',
                     label=labels[1])
    plt.ylabel('coordination')
    plt.title(title)
    plt.xticks(index + bar_width, att)
    plt.legend()
    plt.tight_layout()
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.savefig(os.path.join(directory, name))
    plt.close()


'''
lsm graphs
'''


def calc_avg_over_sessions(lsm_match):
    avg = []
    for pos_lsm in lsm_match:
        avg.append(mean(list(map(float, pos_lsm))))
    return avg


def match_graph_one_dyad(directory, match_along_sessions, dyad_num):
    plt.plot(calc_avg_over_sessions(match_along_sessions))
    plt.xlabel('session number')
    plt.ylabel('pos-tags LSM average')
    plt.title('Pos-tags matching over sessions')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.savefig(os.path.join(directory, str(dyad_num)))
    plt.close()


# only pos/neg use for now..
# def avg_graph(dyad):
#     avg_val = dyad.avg_lsm_score()
#     plt.plot(avg_val)
#     plt.xlabel('session number')
#     plt.ylabel('LSM avg')
#     plt.title('Positive and negative avg over sessions')
#     todo - edit the path before using this function.
#     plt.savefig(str(dyad.dyad_num))
#     plt.close()
