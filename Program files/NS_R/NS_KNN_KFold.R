rm(list=ls())
#Date: Dec 8th, 2018
#Purpose: NS Project - Link Prediction on Flixster Dataset
library(caTools)
library(caret) # Accuracy
library(ggplot2)
library(rpart)
library(rpart.plot)
library(rattle)
#install.packages("xgboost")
library(randomForest)
library(ROCR)
library(pROC)
library(miscTools)
library(pROC)
library(e1071)

#Read data
actual_data <- read.csv(file="SimilarityIndices.csv", header=TRUE, sep=",")


summary(actual_data)

# Check for any missing values:
sum(is.na(actual_data))

# remove missing values
data <- actual_data[complete.cases(actual_data), ]

# Check for any missing values:
sum(is.na(data))

#Convert scores to factor
data$Label <- as.factor(data$Label)
sapply(data, class)
set.seed(1234)

set.seed(101)
index = createDataPartition(data$Label, p = 0.8, list = F )
train = data[index,]
test = data[-index,]

############################################
#Implementing KNN
###########################################
kNN3 <- train(Label~., data = train, method = "knn", 
              maximize = TRUE,
              trControl = trainControl(method = "cv", number = 10),
              preProcess=c("center", "scale"))
ggplot(kNN3) + geom_line() + geom_smooth() + theme_light()

predictedkNN3 <- predict(kNN3, newdata = test)
confusionMatrix(predictedkNN3, test$Label)

