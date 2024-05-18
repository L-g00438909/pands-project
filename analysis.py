# Analysis of Iris dataset.
# 
# Author: LR


# IMPORT LIBRARIES:
import pandas as pd  #dataframe 
import numpy as np  #array for numerical data
import matplotlib.pyplot as plt  #plotting library
import seaborn as sns  #plotting library

# LOAD THE DATASET:
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# INFORMATION ABOUT THE DATASET:

print('\033[1mINFORMATION ABOUT THE IRIS DATASET:\033[0m')
print('\n')

print('\033[1mNumber of rows and columns in the dataset:\033[0m')
print(df.shape)   # print number of rows and columnns.

print('\033[1mFirst 5 rows of the dataset:\033[0m')
print(df.head())  # print first 5 rows.

print('\033[1mLast 5 rows of the dataset:\033[0m')
print(df.tail())  # print last 5 rows.

print('\033[1mNumber of each species in the dataset:\033[0m')
print(df['species'].value_counts())  # print the number of each species in the dataset.

print('\033[1mNumber of missing values in the dataset:\033[0m') # check missing values in the dataset.
print(df.isnull().sum())  # print the number of missing values in each column of the dataset.

# check data types of the columns in the dataset:
print('\033[1mData types of the columns in the dataset:\033[0m')
print(df.dtypes)  # print the data types of the columns in the dataset.


# SUMMARY STATISTICS:
print('\033[1mSummary statistics of the dataset:\033[0m')
print(df.describe())  # print summary statistics of the dataset.


with open('Iris_summary.txt', 'w') as f:  # open a summary text file in write mode to save the information about the dataset.
      print('INFORMATION ABOUT THE IRIS DATASET:', file=f)
      print('_'*70, file=f)
      print('Number of rows and columns in the dataset:', file=f)  
      print(df.shape, file=f)   
      print('_'*70, file=f)
      print('First 5 rows of the dataset:', file=f)  
      print(df.head(), file=f)  
      print('_'*70, file=f)
      print('Last 5 rows of the dataset:', file=f)  
      print(df.tail(), file=f) 
      print('_'*70, file=f)
      print('Number of each species in the dataset:', file=f)  
      print(df['species'].value_counts(), file=f)  
      print('_'*70, file=f)
      print('Number of missing values in the dataset:', file=f) 
      print(df.isnull().sum(), file=f)  
      print('_'*70, file=f)
      print('Data types of the columns in the dataset:', file=f)  
      print(df.dtypes, file=f)  
with open('Summary_statistics.txt', 'w') as f:  
      print('Summary statistics of the dataset:', file=f)
      print(df.describe(), file=f) 
      






# HISTOGRAMS:

# histogram subplots of numerical variables:
fig, axes = plt.subplots(2, 2, figsize=(10,8))
fig.suptitle('Histograms of numerical variables', color='darkblue', fontweight='bold', fontsize='15')
sns.histplot(df, x='sepal_length', hue='species', kde=True, ax=axes[0, 0], palette={'setosa':'blue', 'versicolor':'purple', 'virginica':'magenta'})
sns.histplot(df, x='sepal_width', hue='species', kde=True, ax=axes[0, 1], palette={'setosa':'blue', 'versicolor':'purple', 'virginica':'magenta'} )
sns.histplot(df, x='petal_length', hue='species',kde=True, ax=axes[1, 0], palette={'setosa':'blue', 'versicolor':'purple', 'virginica':'magenta'} )
sns.histplot(df, x='petal_width', hue='species', kde=True, ax=axes[1, 1], palette={'setosa':'blue', 'versicolor':'purple', 'virginica':'magenta'} )
plt.show()

# histogram of sepal width per species:
sns.histplot(data=df, x='sepal_width', hue='species', multiple='stack', kde=False, palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'})
plt.title('Histogram of Sepal Width by Species')
plt.xlabel('Sepal Width')
plt.ylabel('Frequency')
plt.show()

# histogram of sepal length per species:
sns.histplot(data=df, x='sepal_length', hue='species', multiple='stack', kde=False, palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'})
plt.title('Histogram of Sepal Length by Species')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# histogram of petal width per species:
sns.histplot(data=df, x='petal_width', hue='species', multiple='stack', kde=False, palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'})
plt.title('Histogram of Petal Width by Species')
plt.xlabel('Petal Width')
plt.ylabel('Frequency')
plt.show()

# histogram of petal length per species:
sns.histplot(data=df, x='petal_length', hue='species', multiple='stack', kde=False, palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'})
plt.title('Histogram of Petal Length by Species')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()


# BOXPLOTS:

# subplots boxplot of sepal length, sepal width, petal length, petal width per species separated by color   
fig, ax = plt.subplots(2, 2, figsize=(10, 10))
sns.boxplot(data=df, x='species', y='sepal_length', ax=ax[0, 0], hue='species', palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'} )       
sns.boxplot(data=df, x='species', y='sepal_width', ax=ax[0, 1], hue='species', palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'} )
sns.boxplot(data=df, x='species', y='petal_length', ax=ax[1, 0], hue='species', palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'} )
sns.boxplot(data=df, x='species', y='petal_width', ax=ax[1, 1], hue='species', palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'} )
plt.legend()
plt.show()


# PAIRPLOT:

# pairplot of the dataset:
sns.pairplot(df, hue='species', palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'} , diag_kind='kde')
plt.show()

 
# SCATTERPLOTS:

# scatterplot of sepal length vs sepal width per species with regression line:
sns.lmplot(x='sepal_length', y='sepal_width', data=df, hue='species', fit_reg=True, palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'})
plt.ylabel('Sepal Width')
plt.title('Sepal Length vs Sepal Width')
plt.show()

# scatterplot of petal length vs petal width per species with regression line:
sns.lmplot(x='petal_length', y='petal_width', data=df, hue='species', fit_reg=True, palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'} )
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Petal Length vs Petal Width')

plt.show()


# CORRELATION:

# correlation matrix of the dataset:
correlation = df.groupby('species').corr()  # correlation matrix for each species in the dataset.
print(correlation)

# print correlation to a text file:
with open('correlation_matrix.txt', 'w') as f:  # with statement to open the file and close it automatically
        print(correlation, file=f)  # print correlation matrix to the txt file. file=f is used to redirect the correlation matrix to the txt file in f

# correlation heatmap:
# correlation heatmap of numerical variables
numerical_variables =[ 'sepal_length', 'sepal_width', 'petal_length', 'petal_width']
correlation =df[numerical_variables].corr()
sns.heatmap(correlation, annot=True, cmap='viridis')
plt.title('Correlation Heatmap of Numerical Variables', color='darkblue')
plt.savefig('correlation_heatmap.png')

plt.show()
