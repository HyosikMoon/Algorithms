## Author
# Saeed Aghabozorgi
# Other Contributors
# Joseph Santarcangelo


## Objectives
# After completing this lab you will be able to:
# Use scikit-learn to Support Vector Machine to classify
# In this notebook, you will use SVM (Support Vector Machines) to build and train a model using human cell records, and classify cells to whether the samples are benign or malignant.
# SVM works by mapping data to a high-dimensional feature space so that data points can be categorized, even when the data are not otherwise linearly separable. A separator between the categories is found, then the data is transformed in such a way that the separator could be drawn as a hyperplane. Following this, characteristics of new data can be used to predict the group to which a new record should belong.


## Table of contents¶
# Load the Cancer data
# Modeling
# Evaluation
# Practice

# !pip install scikit-learn==0.23.1
import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
# %matplotlib inline 
import matplotlib.pyplot as plt

## Load the Cancer data
# The example is based on a dataset that is publicly available from the UCI Machine Learning Repository (Asuncion and Newman, 2007)[http://mlearn.ics.uci.edu/MLRepository.html]. The dataset consists of several hundred human cell sample records, each of which contains the values of a set of cell characteristics. The fields in each record are:

# Field name	Description
# ID	        Clump thickness
# Clump	        Clump thickness
# UnifSize  	Uniformity of cell size
# UnifShape	    Uniformity of cell shape
# MargAdh	    Marginal adhesion
# SingEpiSize	Single epithelial cell size
# BareNuc	    Bare nuclei
# BlandChrom	Bland chromatin
# NormNucl	    Normal nucleoli
# Mit	        Mitoses
# Class	        Benign or malignant

# For the purposes of this example, we're using a dataset that has a relatively small number of predictors in each record. To download the data, we will use !wget to download it from IBM Object Storage.
#Click here and press Shift+Enter
# !wget -O cell_samples.csv https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/cell_samples.csv

# Load Data From CSV File
cell_df = pd.read_csv("cell_samples.csv")
cell_df.head()
# ID	Clump	UnifSize	UnifShape	MargAdh	SingEpiSize	BareNuc	BlandChrom	NormNucl	Mit	Class
# 0	1000025	5	1	1	1	2	1	3	1	1	2
# 1	1002945	5	4	4	5	7	10	3	2	1	2
# 2	1015425	3	1	1	1	2	2	3	1	1	2
# 3	1016277	6	8	8	1	3	4	3	7	1	2
# 4	1017023	4	1	1	3	2	1	3	1	1	2

# The ID field contains the patient identifiers. The characteristics of the cell samples from each patient are contained in fields Clump to Mit. The values are graded from 1 to 10, with 1 being the closest to benign.
# The Class field contains the diagnosis, as confirmed by separate medical procedures, as to whether the samples are benign (value = 2) or malignant (value = 4).
# Lets look at the distribution of the classes based on Clump thickness and Uniformity of cell size:
ax = cell_df[cell_df['Class'] == 4][0:50].plot(kind='scatter', x='Clump', y='UnifSize', color='DarkBlue', label='malignant');
cell_df[cell_df['Class'] == 2][0:50].plot(kind='scatter', x='Clump', y='UnifSize', color='Yellow', label='benign', ax=ax);
plt.show()


## Data pre-processing and selection
# Lets first look at columns data types:
cell_df.dtypes
# ID              int64
# Clump           int64
# UnifSize        int64
# UnifShape       int64
# MargAdh         int64
# SingEpiSize     int64
# BareNuc        object
# BlandChrom      int64
# NormNucl        int64
# Mit             int64
# Class           int64
# dtype: object

# It looks like the BareNuc column includes some values that are not numerical. We can drop those rows:
cell_df = cell_df[pd.to_numeric(cell_df['BareNuc'], errors='coerce').notnull()]
cell_df['BareNuc'] = cell_df['BareNuc'].astype('int')
cell_df.dtypes
# ID             int64
# Clump          int64
# UnifSize       int64
# UnifShape      int64
# MargAdh        int64
# SingEpiSize    int64
# BareNuc        int64
# BlandChrom     int64
# NormNucl       int64
# Mit            int64
# Class          int64
# dtype: object

feature_df = cell_df[['Clump', 'UnifSize', 'UnifShape', 'MargAdh', 'SingEpiSize', 'BareNuc', 'BlandChrom', 'NormNucl', 'Mit']]
X = np.asarray(feature_df)
X[0:5]
# array([[ 5,  1,  1,  1,  2,  1,  3,  1,  1],
#        [ 5,  4,  4,  5,  7, 10,  3,  2,  1],
#        [ 3,  1,  1,  1,  2,  2,  3,  1,  1],
#        [ 6,  8,  8,  1,  3,  4,  3,  7,  1],
#        [ 4,  1,  1,  3,  2,  1,  3,  1,  1]])

# We want the model to predict the value of Class (that is, benign (=2) or malignant (=4)). As this field can have one of only two possible values, we need to change its measurement level to reflect this.
cell_df['Class'] = cell_df['Class'].astype('int')
y = np.asarray(cell_df['Class'])
y [0:5]
# array([2, 2, 2, 2, 2])


## Train/Test dataset
# Okay, we split our dataset into train and test set: