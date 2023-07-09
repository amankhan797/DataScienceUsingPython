#This .py file contains all the basic operation of pandas library.

import pandas as pd #import library's (pandas and numpy)
import numbers as nm
dict1={
    "name":[ 'Aman' , 'vighnesh' , 'faisal' , 'samad' ],
    "class":['TYBCA','TYBCA','SYBCS','FYBCA'],
    "Marks":['100','100','99','98']
}  #created a dictionary with Key-Value pairs

# DataFrame in pandas is like a table or a spreadsheet for faster indexing and read readibility.
df = pd.DataFrame(dict1)
print(df) #here we are printing th dict in tabular formate
df.to_csv('studentData.csv') #we are creating an CSV file and exporting the data into it

#If we don't need Indexing in CSV file we can use Indexing=False
df.to_csv('studentData_without_indexing.csv',index=False)
print(df)

#if there are million rows then its not possible to see the information properly.
#thats why we are using .head() and .tail() functions.
print(df.head(2))
print(df.tail(1))

#if your data have numericals columns then .describe() function gives ststical analysis.
print(df.describe())

#Let us assume we have an CSV file and you want to read it then we can use .read_csv()
aman = pd.read_csv('Capital.csv')
print(aman)

#if we want to change the content of the CSV file, below is the method to do it.
aman['State'][3]='patna'
print(aman)
#I know its patna is not an state :) but the code is working...

#if U want to change the index U can use .index() function, we can use srtings also.
aman.index = [9,8,7,6]
print(aman)