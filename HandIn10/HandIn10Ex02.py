import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import estimate_bandwidth
from sklearn.cluster import MeanShift
dat = pd.read_csv('./Sem4Python/HandIn10/iris_csv.csv')
#print(dat)
species = dat["Species"].unique()

def plot_data(leaf, plot):
    ax = plot.add_subplot(111)
    colors = ['r', 'b', 'g']

    for spec, color in zip(species, colors):
        s = dat[dat["Species"] == spec]

        x = s[f"{leaf} length"]
        y = s[f"{leaf} width"]

        ax.scatter(x, y, c=color, linewidth=0.2)
    ax.set_title(f"{leaf} length and width")
    ax.legend(species)

plot_data("Sepal", plt.figure())
plot_data("Petal", plt.figure())
plt.show()

def find_meanshift(leaf):
    data = dat[[f"{leaf} length", f"{leaf} width"]]
    bandwidth = estimate_bandwidth(data, quantile=0.2)
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(data)
    clusters = ms.cluster_centers_
    labels = ms.labels_
    number_clusters = len(clusters)
    return labels, clusters, number_clusters

def plot_clusters(leaf, plot): 
    labels, clusters, number_clusters = find_meanshift(leaf)
    ax = plot.add_subplot(111)
    c = ['r', 'b', 'g', 'y']

    for clust, col in zip(range(number_clusters), c):
        center = clusters[clust]
        my_members = labels == clust
        data = dat[[f"{leaf} length", f"{leaf} width"]].to_numpy()
        x, y = data[my_members, 0], data[my_members, 1]
        ax.scatter(x, y, c=col, linewidth=0.2)
        ax.scatter(center[0], center[1], c='k', s=50)
    ax.set_title(f"{leaf} clusters")

plot_clusters("Petal", plt.figure())
plot_clusters("Sepal", plt.figure())
plt.show()

plot_data("Sepal", plt.figure())
plot_clusters("Sepal", plt.figure())
plt.show()

plot_data("Petal", plt.figure())
plot_clusters("Petal", plt.figure())
plt.show()