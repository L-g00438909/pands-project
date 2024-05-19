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
print(df.info())  # information about the dataset


# SUMMARY STATISTICS:
print('\033[1mSummary statistics of the dataset:\033[0m')
print(df.describe())  # print summary statistics of the dataset.
print('\n')





with open('summary_irisdata.txt', 'w') as f:  # open a summary text file in write mode to save the information about the dataset.
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
with open('summary_statistics.txt', 'w') as f:  
      print('Summary statistics of the dataset:', file=f)
      print(df.describe(), file=f)
      print('\n', file=f)
      print('Summary statistics for Iris Setosa:', file=f)
      print(df[df['species']=='setosa'].describe(), file=f)
      print('\n', file=f)
      print('Summary statistics for Iris Versicolor:', file=f)
      print(df[df['species']=='versicolor'].describe(), file=f)
      print('\n', file=f)
      print('Summary statistics for Iris Virginica:', file=f)
      print(df[df['species']=='virginica'].describe(), file=f)
      print('\n', file=f)

      

# DATA VISUALIZATION:



# HISTOGRAMS:

# histogram of sepal width per species:
sns.histplot(data=df, x='sepal_width', hue='species', multiple='stack', kde=True, palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'})
plt.title('Histogram of Sepal Width by Species', color='darkblue', fontsize=15, fontweight='bold')
plt.xlabel('Sepal Width (cm)', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.savefig('histogram_sepal_width.png')
plt.close()

# histogram of sepal length per species:
sns.histplot(data=df, x='sepal_length', hue='species', multiple='stack', kde=True, palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'})
plt.title('Histogram of Sepal Length by Species', color='darkblue', fontsize=15, fontweight='bold')
plt.xlabel('Sepal Length (cm)', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.savefig('histogram_sepal_length.png')
plt.close()

# histogram of petal width per species:
sns.histplot(data=df, x='petal_width', hue='species', multiple='stack', kde=True, palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'})
plt.title('Histogram of Petal Width by Species', color='darkblue', fontsize=15, fontweight='bold')
plt.xlabel('Petal Width (cm)', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.savefig('histogram_petal_width.png')
plt.close()

# histogram of petal length per species:
sns.histplot(data=df, x='petal_length', hue='species', multiple='stack', kde=True, palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'})
plt.title('Histogram of Petal Length by Species', color='darkblue', fontsize=15, fontweight='bold')
plt.xlabel('Petal Length (cm)', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.savefig('histogram_petal_length.png')
plt.close()



# BOXPLOTS:

# subplots boxplot of sepal length, sepal width, petal length, petal width per species separated by color   
fig, ax = plt.subplots(2, 2, figsize=(10, 10))
sns.boxplot(data=df, x='species', y='sepal_length', ax=ax[0, 0], hue='species', palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'} )       
sns.boxplot(data=df, x='species', y='sepal_width', ax=ax[0, 1], hue='species', palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'} )
sns.boxplot(data=df, x='species', y='petal_length', ax=ax[1, 0], hue='species', palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'} )
sns.boxplot(data=df, x='species', y='petal_width', ax=ax[1, 1], hue='species', palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'} )
plt.savefig('boxplots.png')
plt.close()


# CORRELATION PLOTS:


# pairplot of the dataset:
sns.pairplot(df, hue='species', palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'} , diag_kind='kde')
plt.savefig('pairplot.png')
plt.close()
 

# Petal length vs Petal width scatterplot with regression line:
petal_length = df['petal_length'] # petal length
print(petal_length)
print(type(petal_length))
petal_length=df['petal_length'].to_numpy()  # convert petal length to numpy array
print(petal_length)
petal_width = df['petal_width'].to_numpy()  # convert petal width to numpy array
print(petal_width)

m, c = np.polyfit(petal_length, petal_width, 1)  # linear regression line
print('\033[1mSlope and Intercept:\033[0m')
print(m, c)

fig, ax = plt.subplots()
ax.plot(petal_length, petal_width, 'x')
ax.plot(petal_length, m*petal_length + c, 'r-')
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Petal Width (cm)')
ax.set_title('Petal Length vs Petal Width')
plt.text(3, 2, f'y={m:.2f}x+{c:.2f}', color='red', fontsize=10)
plt.savefig('scatterplot_petal.png')
plt.close()


# scatterplot of petal length vs petal width per species with regression line:
sns.lmplot(x='petal_length', y='petal_width', data=df, hue='species', fit_reg=True, palette={'setosa': 'blue', 'versicolor': 'purple', 'virginica': 'magenta'} )
plt.xlabel('Petal Length (cm)', color='darkblue')
plt.ylabel('Petal Width (cm)', color='darkblue')
plt.title('Petal Length vs Petal Width', color='darkblue')
plt.savefig('scatterplot_petal_species.png')
plt.close()





# correlation matrix of the dataset:
print('\033[1mCorrelation matrix of the dataset:\033[0m')
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
plt.close()

