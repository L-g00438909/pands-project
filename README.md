<img src="https://mjconroy.com/wp-content/uploads/2023/04/ATU-Logo.png" width="250" height="150">


### Higher Diploma in Science: Computing-Data Analytics 2024
### Module: Programming and Scripting
*** 



<b>

# <div align="leftcenter">Analysis of the Iris Dataset</div></b>

***


### Objective: 

The objective of this project is to analyse the Fishers Iris dataset using Python. Python libraries such as Pandas, Numpy, Matplotlib, Seaborn are used to explore the data, generate descriptive statistics and create data visualisations to demonstrate trends and relationships within the dataset. 

### Method: 

1.  **Import Libraries:**

 -   Pandas: 
 -   Numpy:
-   Matplotlib:
-   Seaborn:
2.  **Load the dataset:**

-    The dataset was loaded from the URL obtained on the seaborn website into a dataFrame created by Pandas. 

3.  **Exploratory Data Analysis:**
-   Look at information about the dataset. 

4.  **Data Cleaning:**
-   Check the dataset for any missing values. 

5.  **Descriptive Statistics:**
-   Summarise the data

6.  **Data Visualisation:**
-   Matplotlib and seaborn used to visualise the data using Histograms, Boxplots, Pairplots, Scatterplots.

7.  **Conclusion:**
-   summary of findings 



### Background:

The Iris dataset is a multivariate dataset consisting of 50 samples from three species of the Iris flower. Iris Setosa, Iris Versicolor and Iris Virginica. The length and width of the sepals and petals of the flowers were measured to assess the variation in Iris flowers of the three related species. 


<img src="https://media.licdn.com/dms/image/D4D12AQH-T205O9k22g/article-inline_image-shrink_1000_1488/0/1694100871364?e=2147483647&v=beta&t=D3kWufrXHt34EA9NORP4qMsSOR42BNvA1H4e-UjvE3k" width=500 height=200>

The Iris data set was first used by Ronald A. Fisher in 1936 to demonstrate how linear discriminant analysis can be applied to classify data in different categories (species) based on the measurements of the flower features. 
Fisher is said to have created the foundations for modern statistical science. 





# Summary Statistics:
***

<img src='stats_iris.png' height=300 width=400>

The describe() function in pandas generates descriptive statistics of the dataFrame giving a summary of the central tendency, dispersion and shape of the distribution of the dataset. 

Sepal Length: 
-   The mean 5.84cm and median 5.80cm are close indicating a symmetric distribution
-   the standard deviation of 0.83 indicates low variability. 

Sepal Width:
-   the mean 3.06cm and median 3.00cm are close indicating symmetric distribution, with an even lower standard deviation of 0.44 showing low variability. 

Petal Length:
-   The mean of 3.76cm is significantly lower than the median of 4.35cm indicating a left skewed distribution. 
-   A higher standard deviation of 1.76 indicates a higher variability among the data points. 

Petal Width: 
-   The mean of 1.2cm is slightly lower than the median of 1.3cm which could indicate a slightly left skew. 
-   A standard deviation of 0.76 is low




# Data Visualisation:
***
Histograms show the distribution of numerical data by grouping data points that lie within a range of values in to a bin. The higher the bar the greater the frequency of values.


<p float='left'>
<img src="histogram_sepal_width.png" height=400 width=400>
<img src='histogram_sepal_length.png' height=400 width=400>
</p>


<p float='left'>
<img src='histogram_petal_width.png' height=400 width=400>
<img src='histogram_petal_length.png' height=400, width=400>
</p>

From the above histograms it can be seen that there is overlap between all species for sepal width and sepal length. 

Iris setosa is clearly distinguishable from Iris Versicolor and Iris Virginica in petal width and petal length with Iris setosa having the smaller petal lengths and widths and is seen to be clustered at the lower end of the histogram. There is overlap seen between Iris Virginica and Iris Versicolor. 

The higher standard deviation obtained for petal length is more than likely due to the significant difference between the species in petal length. Iris setosa has a mean petal length of 1.46cm in comparison to Iris Versicolor with a mean of 4.26cm and Iris Virginica with a mean of 5.55cm. 

While petal width had a lower standard deviation than petal length it can be seen that Iris Setosa forms a distinct cluster at the lower end of the histogram separate from Iris Versicolor and Iris Virginica. The mean petal width of Iris Setosa of 0.25cm is significantly lower than that of Iris Versicolor with a mean of 1.33cm and Iris Virginica with a mean of 2.03cm. 




#### Correlation:


<img src='pairplot.png' height=500 width=600>
