# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:10:31 2022

@author: Anna
"""

import matplotlib.pyplot as plt
from sklearn.datasets import make_moons,make_circles,make_blobs
import algorithm


color_list = ['Aqua','Black','Fuchsia','Gray','Green','Lime','Maroon','Navy','Olive'
              ,'Purple','Red','Silver','Teal','Yellow','Blue']
name_list = ['circles','moons','Gaussian']
fs = 6
flag = 2
if flag==0:
    ###Generate circles distribution data set
    data,label = make_circles(n_samples=6000, factor=.5,noise=.15)
elif flag==1:
    ###Generate moons distribution data set
    data,label = make_moons(n_samples=6000,noise=0.2)   
else:
    ###Generate Gaussian distribution data set
    m=1.5
    centers = [(0, -m),  (0, m)]
    data, label = make_blobs(n_samples=6000, n_features=2, cluster_std=1.0,
                      centers=centers, shuffle=False, random_state=42)
### Visualize data set
plt.figure(figsize=(fs,fs))
plt.scatter(data[:,0], data[:,1], c=label)
plt.xticks([]) 
plt.yticks([])
plt.savefig("%s.png"%name_list[flag], bbox_inches='tight')
plt.show()

### plot confidence homogeneous cluster
chc = algorithm.Con_LHC(data,label)
plt.figure(figsize=(fs,fs))
for i in range(len(chc)):
    plt.scatter(data[chc[i],0], data[chc[i],1], c=color_list[i%len(color_list)])
plt.xticks([]) 
plt.yticks([])
plt.savefig("%s_hc.png"%name_list[flag], bbox_inches='tight')
plt.show()

### plot reduced data set
rdi= algorithm.BDIS(data,label,-1,7) #reduced data index
plt.figure(figsize=(fs,fs))
plt.scatter(data[rdi,0], data[rdi,1], c=label[rdi])
plt.xticks([]) 
plt.yticks([])
plt.savefig("%s_reduced.png"%name_list[flag], bbox_inches='tight')
plt.show()














