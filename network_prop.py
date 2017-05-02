#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 22:30:17 2017

@author: pk
"""
import pandas as pd
#df = pd.read_csv('/home/pk/Downloads/tij_InVS.dat', sep='\s+', header=None)

df = pd.read_csv('/home/pk/Downloads/primaryschool.csv', sep=',', header=None)
df=df[[1,2]]
fileopen=open("/home/pk/Desktop/np.txt","w")
for i in range(0,len(df.axes[0])):
    line=str(df.iloc[i,0])+"\t"+str(df.iloc[i,1])+"\n"
    fileopen.write(line)


import matplotlib.pyplot as plt
import networkx as nw

nwk1=nw.read_edgelist('/home/pk/Desktop/np.txt',nodetype=int)

n,k=nwk1.order(), nwk1.size()

avg_deg=float(k)/n

degree_sequence=sorted(nw.degree(nwk1).values(),reverse=True)

dmax=max(degree_sequence)

plt.loglog(degree_sequence,'b-',marker='o')

plt.title("degree sequence")
plt.ylabel("fraction of nodes")
plt.xlabel("degree")

plt.axes([0.45,0.45,0.45,0.45])
Gcc=sorted(nw.connected_component_subgraphs(nwk1), key = len, reverse=True)[0]
pos=nw.spring_layout(Gcc)
plt.axis('off')
nw.draw_networkx_nodes(Gcc,pos,node_size=20)
nw.draw_networkx_edges(Gcc,pos,alpha=0.4)

clust_coeff=nw.clustering(nwk1)

ccs=nw.clustering(nwk1)
agv_clust=sum(ccs.values())/len(ccs)

nwk1_components = nw.connected_component_subgraphs(nwk1)
nwk1_mc = nwk1_components[0]
# Betweenness centrality
bet_cen = nw.betweenness_centrality(nwk1)
# Closeness centrality
clo_cen = nw.closeness_centrality(nwk1)
# Eigenvector centrality
eig_cen = nw.eigenvector_centrality(nwk1)

def highest_centrality(cent_dict):
    """Returns a tuple (node,value) with the node
    with largest value from Networkx centrality dictionary."""
    # Create ordered tuple of centrality data
    cent_items=[(b,a) for (a,b) in cent_dict.iteritems()]
    # Sort in descending order
    cent_items.sort()
    cent_items.reverse()
    return tuple(reversed(cent_items[0]))

highest_centrality(bet_cen)
highest_centrality(clo_cen)
highest_centrality(eig_cen)

def centrality_scatter(dict1,dict2,path="",
                       ylab="",xlab="",title="",line=False):
    # Create figure and drawing axis
    fig = plt.figure(figsize=(7,7))
    ax1 = fig.add_subplot(111)
    # Create
    items1 =sorted(dict1.items())
    items2 =sorted(dict2.items())
    xdata=[b for a,b in items1]
    ydata=[b for a,b in items2]
    # Add each actor to the plot by ID
    for p in xrange(len(items1)):
        ax1.text(x=xdata[p], y=ydata[p],s=str(items1[p][0]), color="b")
    
    if line:
# use NumPy to calculate the best fit
        slope, yint = plt.polyfit(xdata,ydata,1)
        xline = plt.xticks()[0]
        yline = map(lambda x: slope*x+yint,xline)
        ax1.plot(xline,yline,ls='--',color='b')
        # Set new x- and y-axis limits
    plt.xlim((0.0,max(xdata)+(.15*max(xdata))))
    plt.ylim((0.0,max(ydata)+(.15*max(ydata))))
    # Add labels and save
    ax1.set_title(title)
    ax1.set_xlabel(xlab)
    ax1.set_ylabel(ylab)
    plt.savefig(path)
    
centrality_scatter(eig_cen,clo_cen)
centrality_scatter(bet_cen,clo_cen)

centrality_scatter(bet_cen,eig_cen) 

plt.title(" eigenvalue vs betweenness centrality")
plt.ylabel("eigenvalue centrality")
plt.xlabel("betweenness centrality")

eigenvalue
closeness
betweenness

ecc=nw.eccentricity(nwk1)

Dia=nw.diameter(nwk1, e=ecc)