A network is a dynamic structure which evolves over time due to the addition and deletion of links and nodes in it. This project tries to predict future associations between two exist- ing nodes that forms a connection or link between them. This problem is called the Link Prediction problem. Several similarity indices such as Common Neighbors (CN), Jaccard Coefficient (JC), Adamic-Adar index (AA), Preferential Attachment (PA) and Resource Al- location (RA) are used for prediction. A supervised machine learning method is also made use of to predict links by considering the calculated similarity indices as features. The ex- periments are conducted on Flixter dataset which is a social network of people with similar taste in movies.

Instructions to run the code

On opening the Program files folder, you get to see the following files

The initial dataset was obtained from http://socialcomputing.asu.edu/datasets/Flixster.
You can download the dataset from the link above to the program folder. We use the file edges.csv for our project.

1. The python file splitDataset.py is used to split the initial dataset into testDataset.csv and trainDataset.csv. These csv files have the nodes and the label as well.

2. The python file createtest.py is used to add non existent edges to the testDataset 

3.The python file calculateScores.py should then be run to calculate the similarity indices of the node pairs. The program execution starts with the creation of the graph. The first node of each edge being added is printed on the screen to keep track of the progress. Once the graph is created, the information regarding the graph is printed on the screen, and then the scores are generated.
PS. The runtime for this code is too long. We have implemented our own algorithms for calculating the scores. We did try using the network inbuilt functions for calculating the scores to check if our code being inefficient was the reason for the long runtime, but this also almost took the same runtime.
The output is obtained in SimilarityIndices.csv
The CSV file will have 8 columns namely
Node1 Node2 CN JI PA AA RA Label

4.The python file calAccuracy.py is to determine the accuracies of all the similarity index models.

5. The python file NsDegCentrality.py determines the degree centrality of the graph and plots a graph.

6. NS_R folder contains the NS_KNN_KFold.R. On executing this file, we get the accuracy of running the KNN algorithm on the data. It also performs-fold cross validation. 
