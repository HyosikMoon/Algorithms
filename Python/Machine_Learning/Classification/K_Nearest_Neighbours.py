## Author
# Saeed Aghabozorgi
# Other Contributors
# Joseph Santarcangelo


## Objectives¶
# After completing this lab you will be able to:
# Use K Nearest neighbors to classify data
# In this Lab you will load a customer dataset, fit the data, and use K-Nearest Neighbors to predict a data point. But what is K-Nearest Neighbors?
# K-Nearest Neighbors is an algorithm for supervised learning. Where the data is 'trained' with data points corresponding to their classification. Once a point is to be predicted, it takes into account the 'K' nearest points to it to determine it's classification.


## Table of contents
# About the dataset
# Data Visualization and Analysis
# Classification


# !pip install scikit-learn==0.23.1
## Lets load required libraries
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# from sklearn import preprocessing
# %matplotlib inline


## About the dataset
# Imagine a telecommunications provider has segmented its customer base by service usage patterns, categorizing the customers into four groups. If demographic data can be used to predict group membership, the company can customize offers for individual prospective customers. It is a classification problem. That is, given the dataset, with predefined labels, we need to build a model to be used to predict class of a new or unknown case.
# The example focuses on using demographic data, such as region, age, and marital, to predict usage patterns.
# The target field, called custcat, has four possible values that correspond to the four customer groups, as follows: 1- Basic Service 2- E-Service 3- Plus Service 4- Total Service
# Our objective is to build a classifier, to predict the class of unknown cases. We will use a specific type of classification called K nearest neighbour.
# Lets download the dataset. To download the data, we will use !wget to download it from IBM Object Storage.
# !wget -O teleCust1000t.csv https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/teleCust1000t.csv


## Load Data From CSV File
df = pd.read_csv('teleCust1000t.csv')
df.head()
## Data Visualization and Analysis
# Let’s see how many of each class is in our data set
df['custcat'].value_counts()
# 281 Plus Service, 266 Basic-service, 236 Total Service, and 217 E-Service customers
# You can easily explore your data using visualization techniques:
df.hist(column='income', bins=50)