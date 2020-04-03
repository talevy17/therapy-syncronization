from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import softmax


# TODO check about the avg

def split_data_to_graph(data, speakers):
    first_graph = {i: [] for i in speakers}
    second_graph = {i: [] for i in speakers}
    for s in range(len(data[0])):
        for i in range(len(speakers)):
            first_graph[speakers[i]].append(softmax(list(data[i][s][0].values())))
            second_graph[speakers[i]].append(softmax(list(data[i][s][1].values())))
    params = len(first_graph[speakers[0]][0])
    return calc_avg(first_graph, speakers, params), calc_avg(second_graph, speakers, params)


def calc_avg(data, speakers, params_n):
    d = {i: [] for i in speakers}
    for s in speakers:
        for c in range(params_n):
            d[s].append(mean(list(data[s][session][c] for session in range(len(data[s])))))
    return d


def c_graphs(coor_all_dyad):
    dyad_dict = {}
    for d in coor_all_dyad:
        # graphs = split_data_to_graph(coor_all_dyad[d], ['speaker', 'target'])
        # plot_graph([graphs[1]['speaker'], graphs[1]['target']],
        #            ['speaker: therapist', 'speaker: client'], d, 'dyad coordination by sessions')
        dyad_dict[d] = split_data_to_graph(coor_all_dyad[d], ['speaker', 'target'])
    return dyad_dict


def merge_data(coor_all_dyad, speakers, att):
    data = c_graphs(coor_all_dyad)
    first_graph = {}
    second_graph = {}
    for s in speakers:
        first_graph[s] = [mean(list(data[d][0][s][a] for d in range(len(data)))) for a in range(att)]
        second_graph[s] = [mean(list(data[d][1][s][a] for d in range(len(data)))) for a in range(att)]
    return first_graph, second_graph


def calc_all_dyad_graph(coor_all_dyad, speakers, att):
    first_g, sec_g = merge_data(coor_all_dyad, speakers, att)
    plot_graph([first_g['speaker'], first_g['target']],
               ['speaker: therapist', 'speaker: client'], 's',
               'Speaker Coordination')
    plot_graph([sec_g['speaker'], sec_g['target']],
               ['target: therapist', 'target: client'], 't',
               'Target Coordination')

def plot_graph(data_bars, labels, name, title):
    fig, ax = plt.subplots()
    index = np.arange(3)
    bar_width = 0.08
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
    plt.xticks(index + bar_width, ('positive', 'negative', 'avg'))
    plt.legend()
    plt.tight_layout()
    plt.savefig(name)


def avg_graph(dyad):
    avg_val = dyad.avg_lsm_score()
    plt.plot(avg_val)
    plt.xlabel('session number')
    plt.ylabel('LSM avg')
    plt.title('Positive and negative avg over sessions')
    plt.savefig(str(dyad.dyad_num))
    plt.show()


def match_graph(dyad):
    match_along_sessions = dyad.get_lsm_dyad()
    plt.plot(match_along_sessions)
    plt.xlabel('session number')
    plt.ylabel('LSM')
    plt.title('Positive and negative matching over sessions')
    plt.savefig(str(dyad.dyad_num))
    plt.show()
