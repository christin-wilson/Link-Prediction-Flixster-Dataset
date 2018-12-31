# This program calculates the accuracies of the similarity indices using the confusion matrices
import networkx as nx
import pandas as pd
import math
# All the values are initialised as 0. yy represent actual and predicted yes while nn represent actual and predicted no.
# ny represents actual no but predicted yes and yn represents actual yes but predicted no.
yyCN=0              
yyAA=0
yyJI=0
yyPA=0
yyRA=0
nnCN=0
nnAA=0
nnJI=0
nnyA=0
nnRA=0
ynCN=0
ynAA=0
ynJI=0
ynyA=0
ynRA=0
nyCN=0
nyAA=0
nyJI=0
nyyA=0
nyRA=0
df = pd.read_csv('SimilarityIndices.csv')      # The similarity indices values are loaded
for i, row in df.iterrows():
	if(row[7]==0):							   # Checks for an actual no.
		if(row[2]<4):
			nnCN+=1
		else:
			nyCN+=1

		if(row[3]<0.037):					   #Checks for predicted yes or predicted no for each similarity index.
			nnJI+=1
		else:
			nyJI+=1
		if(row[4]<6105.753):
			nnyA+=1
		else:
			nyyA+=1
		if(row[5]<2.4):
			nnAA+=1
		else:
			nyAA+=1
		if(row[6]<0.084):
			nnRA+=1
		else:
			nyRA+=1				
	if(row[7]==1.0):							# Checks for an actual yes.
		if(row[2]>3.99):
			yyCN+=1
		else:
			ynCN+=1
		if(row[3]>0.036):
			yyJI+=1
		else:
			ynJI+=1
		if(row[4]>6105):						# Checks for predicted yes or predicted no for each similarity index.
			yyPA+=1
		else:
			ynyA+=1
		if(row[5]>2.39):
			yyAA+=1
		else:
			ynAA+=1
		if(row[6]>0.083):
			yyRA+=1
		else:
			ynRA+=1	
print("CN")						
print("nn: "+str(nnCN)+"ny: "+str(nyCN))		# Prints confusion matrix
print("yn: "+str(ynCN)+"yy: "+str(yyCN))
num=int(nnCN)+int(yyCN)
den=int(nnCN)+int(nyCN)+int(ynCN)+int(yyCN)
print("accuracy:")
print(num/float(den))							#prints accuracy for the model

print("JI")						
print("nn: "+str(nnJI)+"ny: "+str(nyJI))
print("yn: "+str(ynJI)+"yy: "+str(yyJI))
num=int(nnJI)+int(yyJI)
den=int(nnJI)+int(nyJI)+int(ynJI)+int(yyJI)
print("accuracy:")
print(num/float(den))

print("PA")						
print("nn: "+str(nnyA)+"ny: "+str(nyyA))
print("yn: "+str(ynyA)+"yy: "+str(yyPA))
num=int(nnyA)+int(yyPA)
den=int(nnyA)+int(nyyA)+int(ynyA)+int(yyPA)
print("accuracy:")
print(num/float(den))

print("AA")						
print("nn: "+str(nnAA)+"ny: "+str(nyAA))
print("yn: "+str(ynAA)+"yy: "+str(yyAA))
anum=int(nnAA)+int(yyAA)
den=int(nnAA)+int(nyAA)+int(ynAA)+int(yyAA)
print("accuracy:")
print(num/float(den))

print("RA")						
print("nn: "+str(nnRA)+"ny: "+str(nyRA))
print("yn: "+str(ynRA)+"yy: "+str(yyRA))
num=int(nnRA)+int(yyRA)
den=int(nnRA)+int(nyRA)+int(ynRA)+int(yyRA)
print("accuracy:")
print(num/float(den))
