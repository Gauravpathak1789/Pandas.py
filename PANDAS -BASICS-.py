#!/usr/bin/env python
# coding: utf-8

# Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series

# In[4]:


import pandas as pd
pd.Series([4,8,15,16,23])


# Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the 
# variable print it.

# In[5]:


list1=[7,8,"gaurav",89,True,2+7j,"html","pw",99]
print(pd.Series(list1))


# Q3. Create a Pandas DataFrame that contains the following data:
# 
# Name
# Alice
# Bob
# Claire
#             Age
#             25
#             30
#             27
#                                         Gender
#                                         Female
#                                         Male
#                                         Female
# Then, print the DataFrame.

# In[7]:


data={'Name':["Alice","Bob","Clair"],"Age":[25,30,27],"Gender":["Female","Male","Female"]}
pd.DataFrame(data,index=None)


# Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.

# In[8]:


#DataFrame in pandas is the representation of dat in tabular structure where columns and rows are labelled.
#it is different from pandas.Series as Series doesn't have columns labeled on it as DataFrame have 
#example -------we can refer DaaFrame as table of excel sheet and the column data is known as series.


# Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can 
# you give an example of when you might use one of these functions?

# In[9]:


#drop(): This function is used to remove one or more columns or rows from the DataFrame. For example, if we have a DataFrame with a column that we don't need, we can use the drop() function to remove it:
#fillna(): This function is used to replace missing values with a specified value or a calculated value. For example, if we have missing values in a DataFrame, we can use the fillna() function to replace them with a mean value of that column:
#groupby(): This function is used to group rows in a DataFrame by one or more columns and apply a function to each group. For example, if we have a DataFrame with sales data, we can group it by the salesperson's name and calculate the total sales made by each person:


# Q6. Which of the following is mutable in nature Series, DataFrame, Panel?

# In[10]:


#In pandas, both Series and DataFrame are mutable in nature, while Panel is considered deprecated and is no longer recommended for use in recent versions of pandas.

#A mutable object is one that can be modified after it is created. In the context of pandas, this means that we can modify the values, add or remove rows or columns, or change the data types of the elements in a Series or DataFrame after it has been created.


# Q7. Create a DataFrame using multiple Series. Explain with an example.

# In[12]:


s1=[12,"gaurav",True]
s2=[90,67,"dil"]
s3=["i","love","you"]
pd.DataFrame([s1,s2,s3])


# In[ ]:




