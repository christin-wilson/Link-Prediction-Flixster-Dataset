On opening the Program files folder, you get to see the following files

The initial dataset was obtained from http://socialcomputing.asu.edu/datasets/Flixster
It is saved as the file edges.csv. 

1. The python file splitDataset.py was used to split the initial dataset into testDataset.csv and trainDataset.csv. These csv files have the nodes and the label as well.

2. The python file createtest.py was used to add non existent edges to the testDataset 

3.The python file calculateScores.py is then run to calculate the similarity indices of the node pairs. The program execution starts with the creation of the graph. The first node of each edge being added is printed on the screen to keep track of the progress. Once the graph is created, the information regarding the graph is printed on the screen, and then the scores are generated.
PS. The runtime for this code is too long. We have implemented our own algorithms for calculating the scores. We did try using the network inbuilt functions for calculating the scores to check if our code being inefficient was the reason for the long runtime, but this also almost took the same runtime.
The output is obtained in SimilarityIndices.csv
The CSV file will have 8 columns namely
Node1 Node2 CN JI PA AA RA Label

4.The python file calAccuracy.py is then run to determine the accuracies of all the similarity index models.

5. The python file NsDegCentrality.py determines the degree centrality of the graph and plots a graph.

6. NS_R folder contains the NS_KNN_KFold.R. On executing this file, we get the accuracy of running the KNN algorithm on the data. It also performs-fold cross validation. 