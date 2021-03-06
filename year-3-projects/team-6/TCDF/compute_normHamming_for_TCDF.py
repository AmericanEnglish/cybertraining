import numpy as np
from scipy.spatial import distance


def dist_between_matrices_normHamming(A,B):
    return distance.hamming(A.flatten(),B.flatten())

#############################################

graph_Yiyi=np.array([[0,0,0,1,1,0,1,1,1,1,1,0],
                      [0,0,0,0,0,0,0,0,1,0,0,0],
                      [0,0,0,0,0,0,0,0,1,0,0,0],
                      [1,0,0,0,0,1,1,1,1,0,0,1],
                      [1,0,1,0,0,1,0,0,1,1,1,0],
                      [0,0,1,0,1,0,0,0,0,1,1,0],
                      [1,0,0,0,0,0,0,0,1,0,0,0],
                      [1,0,0,0,0,0,0,0,1,0,0,0],
                      [1,1,1,1,0,0,1,1,0,0,0,0],
                      [1,1,1,0,1,1,0,0,0,0,0,0],
                      [1,1,1,0,1,1,0,0,0,0,0,0],
                      [0,0,1,1,0,1,0,0,0,0,0,0]])

graph_h0k2=np.array([[0,0,0,0,0,0,0,0,0,0,0,0], # test 1: hidden_layer=0, kernel_size=2
            [0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,1,0,0,0,0],
                  	[0,0,0,0,0,0,1,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0]])
graph_h0k4=np.array([[0,0,0,0,0,0,0,0,0,0,0,0], # test 2: hidden_layer=0, kernel_size=4
            [0,0,0,0,0,0,0,0,0,0,1,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,1,0,0,0,0,0,0,1],
                  	[1,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,1,0,0,0,0],
                  	[1,0,0,0,0,0,1,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,1,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,1,0,0,0,0,0,0,0,0]])
graph_h0k6=np.array([[0,0,0,0,0,0,0,0,0,0,0,0], # test 3: hidden_layer=0, kernel_size=6
            [0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,1,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0]])
graph_h1k2=np.array([[0,0,0,0,0,0,0,0,0,0,0,0], # test 4: hidden_layer=1, kernel_size=2
            [0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,1,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,1,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,1,0,0,0,0,0,0,0,0,0]])
graph_h1k4=np.array([[0,0,0,0,0,0,0,0,0,0,0,0], # test 5: hidden_layer=1, kernel_size=4
            [0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0]])
graph_h1k6=np.array([[0,0,0,0,0,0,0,0,0,0,0,0], # test 6: hidden_layer=1, kernel_size=6
            [0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0],
                  	[0,0,0,0,0,0,0,0,0,0,0,0]])

###
graphs = [graph_h0k2,graph_h0k4,graph_h0k6,graph_h1k2,graph_h1k4,graph_h1k6,graph_Yiyi]

# Compute normHamming for six verse yiyi ground truth
normH_dis = []
for graph1 in graphs:
    for graph2 in graphs:
        normH_dis.append(dist_between_matrices_normHamming(graph1,graph2))

cnt=0
for i in range(len(normH_dis)):
    cnt += 1
    print("{:.2f}".format(normH_dis[i]),end="\t")
    #print("normH="+ str(shd_dis[i]),end="  ")
    if (7 == cnt):
        cnt=0
        print()
