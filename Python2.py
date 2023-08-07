#CSV file used for below code is Ecommerce Purchases.csv;
# Go to the below link for outputs on Google collab.
# https://colab.research.google.com/drive/115c3DRUGXyN-KSLik6vNlcDK01no5d8M?usp=sharing 

# First we need to import essential libraris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

#Q1 Read the given dataset "Ecommerce purchases" using pandas library?
df=pd.read_csv("/content/Ecommerce Purchases.csv")
df

# Q2 Read all the relevant information about the dataset and get the descriptive statistics of dataset?
df.describe()

# Q3. What is highest lowest and average purchase price?
min = df['Purchase Price'].min()
max=df['Purchase Price'].max()
average=df['Purchase Price'].mean()

print(min)
print(max)
print(average)

# Q4. How many people have English as their language of choice on the website?
count=0
for i in df['Language']:
  if i=="en":
    count=count+1
print(count)

# Q5. How many people has job title "Lawyer"?
count=0
for i in df['Job']:
  if i=="Lawyer":
    count=count+1
print(count)

# Q6. How many people have made purchase during the AM and how many people have made purchase during PM?
c1=0
c2=0
for i in df['AM or PM']:
  if i=="AM":
    c1=c1+1
  else:
    c2=c2+1
print(c1)
print(c2)

# Q7 what are 5 most common job titles?
most_common_jobs = df["Job"].value_counts().head(5)
print(most_common_jobs)

# Q8 what is the email of the person with following credit Card Number: 4926535242672853
df[df['Credit Card']==676344000000]['Email']

# Q9 Histogram of purchase column:
df.hist('Purchase Price', bins=10000) #bins is used to give column count

# Q10 Heatmap of coorelated data
sn.heatmap(df.corr(), annot=True)

# Q11 Heatmap of coorelated data with min and max attributes.
sn.heatmap(df.corr(), vmin=-1 , vmax=5)

# here we are creating heatmap on an array data for better understang of heatmap attributes and function.
df = np.random.randint(1,5, size=(6,6))

#generated array :
#   array([[2, 3, 4, 3, 3, 1],
#           [4, 3, 2, 4, 4, 4],
#           [3, 3, 2, 4, 2, 2],
#           [1, 2, 4, 4, 4, 2],
#           [3, 2, 1, 1, 2, 1],
#           [2, 4, 4, 2, 3, 3]])

sn.heatmap(df, annot=True, vmin=1, vmax=4, cmap='viridis', linewidths=1, linecolor='black', center=2, cbar=False)

#the output is beautyfull & understandable