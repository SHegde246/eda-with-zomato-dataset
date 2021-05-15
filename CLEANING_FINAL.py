#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import math
from scipy import stats
from statistics import mode


# In[11]:


df=pd.read_csv("C:\\Users\\sneha\\OneDrive\\Documents\\SEM_3_STUFF\\IDS_project\\zomato-bangalore-restaurants\\zomato.csv")


# CLEANING

# In[12]:


#'name', 'address'

#dictionary with name:[address1,address2,---]
d=dict()
for i,name in df["name"].iteritems():       # if rest name not in dict, add it(as a key), with addr(as value) in list
    if name not in d:
        d[name]=[]
        d[name].append(df["address"].loc[i])
    else:                                 # name already there
        if df["address"].loc[i] not in d[name]:         #same name, diff addr (diff branch of same rest)
            d[name].append(df["address"].loc[i])        
        else:                                          #duplicate. same name, same addr. drop
            df.drop(i,axis=0,inplace=True)


# In[13]:


# 'online_order' and 'book_table' already clean


# In[14]:


#'rate' aka 'ratings'

df.rename(columns={'rate':'ratings'},inplace=True)

for i,j in df['ratings'].iteritems():
        
    #removing "/5" and converting to float
    if str(j).find("/")!=-1:
        k=j.split("/")
        df['ratings'].loc[i]=float(k[0])
    #dropping other values
    elif j=="-" or j=="NEW" or math.isnan(j):
        df.drop(i,axis=0,inplace=True)


# In[15]:


#'votes'

#replacing 0 values with median
for i,j in df['votes'].iteritems():
    if j==0:
        df['votes'].loc[i]=int(np.median(df.votes))


# In[16]:


#'location' aka 'city_specifics'

df.rename(columns={'location':'city_specifics'},inplace=True)

#city_specifics already cleaned


# In[17]:


#'rest_type'

#list with non nan values
non_nan_rest_type=[]
for i,j in df['rest_type'].iteritems():
    if type(j)==str:
        r_arr=j.split(",")
        for item in r_arr:
            non_nan_rest_type.append(item.lstrip())

#replace nan values with mode
for i,j in df['rest_type'].iteritems():
    if type(j)!=str:
        df['rest_type'].loc[i]=mode(non_nan_rest_type)


# In[18]:


#dish_liked


# In[19]:


#'cuisines'

#to find mode, create list of cuisines
cuisine_list=[]
for i,j in df['cuisines'].iteritems():
    if type(j)==str:
        c_arr=j.split(",")
        for item in c_arr:
            cuisine_list.append(item.lstrip())
            
#repl missing val with mode
for i,j in df['cuisines'].iteritems():
    if type(j)!=str:
        df['cuisines'].loc[i]=mode(cuisine_list)


# In[21]:


#'approx_cost(for two people)' aka 'approx_cost'

df.rename(columns={'approx_cost(for two people)':'approx_cost'},inplace=True)

#converting all non nan values to int
for i,j in df['approx_cost'].iteritems():
    if type(j)==str:
        if j.find(",")!=-1:
            l=int(j.replace(",",""))
            df['approx_cost'].loc[i]=l
        else:
            df['approx_cost'].loc[i]=int(j)
   # elif math.isnan(j):
    #    df['approx_cost'].loc[i]=int(np.mean(lac))
    
#list of all non nan costs
lac=[item for item in list(df.approx_cost) if not(math.isnan(float(item)))]
df.approx_cost = df.approx_cost.fillna(np.mean(lac))


# In[22]:


#'reviews_list'

#'reviews_list' already clean


# In[23]:


#menu_item


# In[24]:


#'listed_in(type)''
df.rename(columns={'listed_in(type)':'meal_type'},inplace=True)
#'listed_in(type)' aka 'meal_type' already clean


# In[25]:


#listed_in(city)
df.rename(columns={'listed_in(city)':'city'},inplace=True)
#'listed_in(city)' aka 'city' already clean 


# In[26]:


df.to_csv("C:\\Users\\sneha\\OneDrive\\Documents\\SEM_3_STUFF\\IDS_project\\final_project_stuff\\cleaned_zomato_final.csv",columns=["name","address","online_order","book_table","ratings","votes","city_specifics","rest_type","dish_liked","cuisines","approx_cost","reviews_list","menu_item","meal_type","city"])


# *******************************************
