# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:03:58 2022

@author: Anna
"""
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import faiss

def Con_LHC(data,label):
    n = len(label)       #dataset size
    cluster_list = []     #homogeneous cluster list
    cluster_centers = []  #homogeneous cluster centers list
    cluster_temp = [np.arange(n)]
    s = 4
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
    for i in range(len(cluster_list)):
        if len(cluster_list[i])>s:
            chc.append(cluster_list[i])
    return chc


def BDIS(data, label, t1,t2):
    n = len(label)       #dataset size
    cluster_list = []     #homogeneous cluster list
    cluster_centers = []  #homogeneous cluster centers list
    cluster_temp = [np.arange(n)]
    s=4
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
    ### Remove redundant samples
    remain_ind = []
    tau1, tau2 = np.int(np.log10(n))+t1, np.int(np.log10(n))*t2
    for i in range(len(cluster_list)):
        cli = cluster_list[i]
        cci = cluster_centers[i]
        if len(cli)>tau1 and len(cli)<tau2:
            neigh = KNeighborsClassifier(n_neighbors=len(cli)-1)
            neigh.fit(data[cli,:], label[cli])
            k_data = neigh.kneighbors(cci.reshape(1,-1), return_distance=False)[0]
            remain_ind.append(cli[k_data[0]])

    return remain_ind