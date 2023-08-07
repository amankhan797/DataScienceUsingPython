#CSV file used for below code is Aman.csv (User Define file for beginning).
# Go to the below link for outputs on Google collab.
# https://colab.research.google.com/drive/115c3DRUGXyN-KSLik6vNlcDK01no5d8M?usp=sharing 

# First we need to import essential libraris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Q1. Read the given dataset using pandas library.
df = pd.read_csv("/content/Aman.csv")
df

# Q2. Find all relevant information about the dataset.
df.info()

# Q3. Get the descriptive statistics of the dataset.
df.describe()

# Q4. Find missing values in the dataset and if exists fill in the missing data with appropriate values .
df.isna().sum()

# Q5. Plot a pie chart for the appropriate columns in the dataset
df["Age"].plot.pie(labels=df.Age )

# Q6. Plot a bar chart for the appropriate columns in the dataset
df.plot.bar(x="Name" , y= "Age")

# Q7. Plot a box plot for the appropriate columns in the dataset
df.plot.box(y= "Age")

# Q8. Plot a scatter plot for the appropriate columns in the dataset
x= [1,2,3]
y= [9,8,7]
plt.scatter(x, y)
plt.show()

# Q9. Plot the histogram for the appropriate columns in the dataset and visualize their distribution.
df['Age'].plot(kind='hist')

# Q10. Plot a heatmap to identify any correlation between the columns.
sns.heatmap(df.corr())