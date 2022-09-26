import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

font_1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font_2 = {'family': 'serif', 'color': 'darkred', 'size': 15}


def dictionary_to_output(idea):
    print("===========")
    print("IDEA INFO")
    for key in idea:
        if idea[key]:
            print(key, ": ", idea[key])
    print("===========")
    return idea


def plot_key_graph(dict_to_plot, title, xlabel_name, ylabel_name):
    x_values = dict_to_plot.keys()
    y_values = dict_to_plot.values()
    plt.bar(x_values, y_values)
    plt.title(title, fontdict=font_1)
    plt.xlabel(xlabel_name, fontdict=font_2)
    plt.ylabel(ylabel_name, fontdict=font_2)
    plt.show()
