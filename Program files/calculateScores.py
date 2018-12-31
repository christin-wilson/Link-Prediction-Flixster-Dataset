#This program calculates the simmilarity indices of the node pairs
import networkx as nx
import pandas as pd
import math
import csv

def calcScores(node1,node2,G):      #function that calculates the scores
	edlist1=[]
	edlist2=[]
	AA=0
	RA=0
	for ed in G.edges():             
		if node1==ed[0]:
			edlist1.append(ed[1])   #Finds the neighbours of the first node and adds to the list
		elif node1==ed[1]:
			edlist1.append(ed[0])
		elif node2==ed[0]:
			edlist2.append(ed[1])   #Finds the neighbours of the second node and adds to the list
		elif node2==ed[1]:
			edlist2.append(ed[0])	
	edlist3 = [value for value in edlist1 if value in edlist2]   #Finds the intersection of the two lists, i.e. the common neighbours
	edlist4 = list(set(edlist1) | set(edlist2))  #Finds the union of the two lists.
	CN=len(edlist3)                 #Calculates Common Neighbors index
	JI=CN/float(len(edlist4))		#Calculates Jaccard Coefficient
	PA=len(edlist1)*len(edlist2)	#Calculates Preferential Attachment
	for z in edlist3:
		x= len(nx.edges(G,[z]))
		den2=1.0/x					
		den=1.0/math.log10(x)
		AA+=den2					#Calculates Adamic-Adar Score
		RA+=den2					#Calculate resource Allocation score
	return(node1,node2,CN,JI,PA,AA,RA) #Returns a list with the score values

df = pd.read_csv('trainDataset.csv') #Read Train Dataset
df2=pd.read_csv('testDataset.csv')	 #Read Test Dataset
G = nx.Graph()						 #Create graph
file1 = open("SimilarityIndices.txt","a") 		
for i, row in df.iterrows():	
	if(row[2]==1):
		G.add_edge(row[0], row[1], attr_dict=row[2:].to_dict())	#Add nodes and edges from  training dataset
		print(row[0])
print(nx.info(G))    				#prints the information of the graph created
for i,row in df2.iterrows():
	x=calcScores(row[0],row[1],G)	#call function to calculate similarity indices
	j= (str(x[0])+","+str(x[1])+","+str(x[2])+","+str(x[3])+","+str(x[4])+","+str(x[5])+","+str(x[6])+","+str(row[2]))
	print(j)
	file1.write(j+"\n")	 
	#convert txt file to csv
with open("SimilarityIndices.txt", 'r') as infile, open('SimilarityIndices.csv', 'w') as outfile:
	stripped = (line.strip() for line in infile)
	lines = (line.split(",") for line in stripped if line)
	print lines
	writer = csv.writer(outfile)
	writer.writerows(lines)	
	
