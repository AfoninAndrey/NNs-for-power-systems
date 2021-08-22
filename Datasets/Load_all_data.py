import time 
import pandas as pd
import numpy as np
from scipy import *
from numpy import dot, multiply, diag, power
from numpy import pi, exp, sin, cos, cosh, tanh, real, imag
from numpy.linalg import inv, eig, pinv,norm
from scipy.linalg import svd, svdvals
import tensorflow as tf
import os
import matplotlib.pyplot as plt
from io import BytesIO
from functools import partial    
import scipy.io as sio 
import time  
import re

def load_data(w,path,name): 
    global   buses 
    PathName = os.path.join(path, name)
    data=sio.loadmat(PathName); 
    dV= data['dV_feature'] # 'dV_feature' is the feature defined in the paper
    Y_ad= data['Y'] # 'Y' is the admittance matrix
    train_data = (Y_ad[:,w] @ dV[w,:]).imag.T   
    train_labels = data['y_num'] 
    col, buses = np.shape(train_data)  
    train_x = np.float64(np.reshape(train_data, (int(col), buses,1)))  
    train_y = np.zeros((int(col ), n_classes))
    for i in range(int(col )):
        train_y[i,train_labels[0][i] ] = 1;
    train_label = np.argmax(train_y,1) 
    return train_x, train_label ,col

def load_all_data(w):
    global train_data, train_labels, train_num, test_data, test_labels, test_num, samples,buses 
    train_data, train_labels, train_num = load_data(w,rootPath, trainName)  
    test_data, test_labels,test_num= load_data(w,rootPath, testName)  
    samples,buses, times  = np.shape(train_data)


fault_type = 1# you can choose from 0 - 3: 
                                        #0 is three phase short circuit; 
                                        #1 is line to ground (LG); 
                                        #2 is double line to ground (DLG); 
                                        #3 is line to line (LL) faults.
impe_type =1# If you choose fault_type from 1 to 3, the impe_type is in the range of 1 to 5, representing different impedance; 
            # If you choose fault_type = 0, the impe-type is 1 to 2, representing different initial conditions;

n_classes=87 
buses = 68
trainName ='Training/Line_faults_train'   
testName = 'Testing/Line_faults_test' +'_type_' + str(fault_type) + '_'+str(impe_type) 
rootPath = 'E:/'# change to where the dataset is located
w=[i for i in range(68)]; # w is the set of the measured buses, e.g. here 0 represents bus 1.
load_all_data(w )
 
''' Then you can use the following training and testing datasetes and labels:'''
train_data  
train_labels 
test_data
test_labels
 
 
 