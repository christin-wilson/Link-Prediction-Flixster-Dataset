# Program to create random non existent edges that are to be added to the test dataset
import random
import networkx as nx
import pandas as pd

df = pd.read_csv('dataset.csv')
G = nx.Graph()
file1 = open("testdataset2.txt","a") 
for i, row in df.iterrows():
    G.add_edge(row[0], row[1], attr_dict=row[2:].to_dict())
    print(row[0])
for ed in G.edges():
	z=[]
	z=nx.edges(G,[ed[0]])	
	x=random.randrange(1,500,1)       # random value generated
	flag=0
	for l in z:					
		if(x == l):					  # check if the edge actually exists
			flag=1
	if(flag==0):
		j= (str(ed[0])+","+str(x)+",0")   # add the node pair with label 0
		file1.write(j+"\n")	

with open("testDataset2.txt", 'r') as infile, open('testDataset.csv', 'a') as outfile:
	stripped = (line.strip() for line in infile)
	lines = (line.split(",") for line in stripped if line)
	print lines
	writer = csv.writer(outfile)
	writer.writerows(lines)	



	

