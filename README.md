# Which Neural Network to Choose in Power Systems]{Which Neural Network to Choose for Post-Fault Localization, Dynamic State Estimation  \& Optimal Measurement Placement in Power Systems?

Source: https://arxiv.org/abs/2104.03115

We consider a power transmission system monitored with Phasor Measurement  Units (PMUs) placed at significant, but not all, nodes of the system. Assuming that a sufficient number  of distinct single-line faults, specifically pre-fault state and (not cleared) post-fault state, are recorded by the PMUs and are  available for training, we, first, design a comprehensive sequence of Neural Networks (NNs) locating the faulty line. Performance of different NNs in the sequence, including Linear Regression, Feed-Forward  NN, AlexNet, Graph Convolutional NN,  Neural Linear Ordinary Differential Equations(ODE) and Neural Graph-based ODE, ordered according to the type and amount of the power flow physics involved, are compared for different levels of observability. Second, we build a sequence of advanced Power-System-Dynamics-Informed and Neural-ODE based Machine  Learning schemes  trained, given pre-fault state, to predict the post-fault  state and  also, in parallel, to estimate system parameters.  Finally, third, and continuing to work with the first (fault localization) setting we design a (NN-based) algorithm which discovers optimal PMU placement. 

## Experiment files:
  - [Detection of Failure](https://github.com/AfoninAndrey/NNs-for-power-systems/blob/main/StaticConfig.ipynb)
  - [Dynamic State Estimation](https://github.com/AfoninAndrey/NNs-for-power-systems/blob/main/DynamicConfig.ipynb)
  - [Optimal Placement of PMUs](https://github.com/AfoninAndrey/NNs-for-power-systems/blob/main/BusImportance.ipynb)
