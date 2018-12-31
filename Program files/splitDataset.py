#This program is used to split the original dataset file to Training and Testing Dataset.
import pandas as pd
import random
import csv
df = pd.read_csv('edges.csv')              # The Original Dataset
file1 = open("testDataset.txt","a")        # The Testing Dataset
file2 = open("trainDataset.txt","a")       # The Training Dataset
for i, row in df.iterrows():
	# Randomfunction used to choose random edges to be hidden in training Dataset
	y=random.randrange(0,400,1)
	if(y==90):									   
		j= (str(row[0])+","+str(row[1])+",1")	#Hidden edge added to Test Data set with label 1	
		file1.write(j+"\n")
		j= (str(row[0])+","+str(row[1])+",0")   #Hidden edge added to Training Data set with label 0
	else:
		j= (str(row[0])+","+str(row[1])+",1")   #Normal existing edges added to Training Data set with label 1
	file2.write(j+"\n")

file1.close()
file2.close()
# The CSV files creation for Test and Train Datasets
with open("testDataset.txt", 'r') as infile, open('testDataset.csv', 'w') as outfile:
	stripped = (line.strip() for line in infile)
	lines = (line.split(",") for line in stripped if line)
	print lines
	writer = csv.writer(outfile)
	writer.writerows(lines)	
	
with open("trainDataset.txt", 'r') as infile, open('trainDataset.csv', 'w') as outfile:
	stripped = (line.strip() for line in infile)
	lines = (line.split(",") for line in stripped if line)
	print lines
	writer = csv.writer(outfile)
	writer.writerows(lines)	