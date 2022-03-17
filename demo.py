# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:10:31 2022

@author: Anna
"""

import numpy as np
import matplotlib.pyplot as plt
import faiss
from sklearn.datasets import make_moons,make_circles

# data,label = make_circles(n_samples=6000, factor=.5,noise=.15)
data,label = make_moons(n_samples=6000,noise=0.2) 
n = len(label)       #dataset size
cluster_list = []     #homogeneous cluster list
cluster_centers = []  #homogeneous cluster centers list
cluster_temp = [np.arange(n)]
s = 2
while cluster_temp:
    ind_cur = cluster_temp[0]
    if len(ind_cur)>s:
        kmeans = faiss.Kmeans(d=data[ind_cur,:].shape[1], k=2, niter=300)
        kmeans.train(data[ind_cur,:].astype(np.float32))
        
        cluster1_ind = ind_cur[np.where(kmeans.index.search(data[ind_cur,:].astype(np.float32), 1)[1]==0)[0]]
        cluster2_ind = ind_cur[np.where(kmeans.index.search(data[ind_cur,:].astype(np.float32), 1)[1]==1)[0]]
        cluster1, cluster2 = kmeans.centroids
    
        if len(set(label[cluster1_ind].ravel()))==1:
            cluster_list.append(cluster1_ind)
            cluster_centers.append(cluster1)
        else:
            if len(cluster1_ind)>s:
                if set(cluster1_ind)&set(ind_cur)!=set(cluster1_ind)|set(ind_cur):
                    cluster_temp.append(cluster1_ind)
        if len(set(label[cluster2_ind].ravel()))==1:
            cluster_list.append(cluster2_ind)
            cluster_centers.append(cluster2)
        else:
            if len(cluster2_ind)>s:
                if set(cluster2_ind)&set(ind_cur)!=set(cluster2_ind)|set(ind_cur):
                    cluster_temp.append(cluster2_ind)
        del cluster_temp[0]
    else:
        del cluster_temp[0]

chc = []    #confidence_homogeneous_cluster with size larger than 2
for cl in cluster_list:
    if len(cl)>s:
        chc.append(cl)
        
### plot confidence homogeneous cluster
#%%
color_list = ['Aqua','Black','Fuchsia','Gray','Green','Lime','Maroon','Navy','Olive'
              ,'Purple','Red','Silver','Teal','Yellow','Blue']

pesu_label = [i+1 for i in range(len(chc))]
fs = 10
plt.figure(figsize=(fs,fs))
for i in range(len(chc)):
    plt.scatter(data[chc[i],0], data[chc[i],1], c=color_list[i%len(color_list)])
plt.xticks([]) 
plt.yticks([])
plt.savefig("moon_hc.png", bbox_inches='tight')
plt.show()


















