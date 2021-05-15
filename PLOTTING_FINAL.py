#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns


# In[17]:


df=pd.read_csv("C:\\Users\\sneha\\OneDrive\\Documents\\SEM_3_STUFF\\IDS_project\\final_project_stuff\\cleaned_zomato_final.csv")


# In[277]:


df.drop(df.columns[0], axis=1)


# *************************************

# In[252]:


#plot the count of rating.
#plt.rcParams['figure.figsize'] = 14,7
g=sns.countplot(df["ratings"], palette="Set1")
g.set_title("Count plot of ratings",fontsize=20,color="blue")
g.set_ylabel("count",fontsize=15,color="green")
g.set_xlabel("ratings",fontsize=15,color="green")
plt.show()


# In[ ]:


###################################################################################################################


# In[19]:


import pandas_profiling
df.profile_report()


# In[60]:


#what % of restaurants have online order option

labels="Yes","No"
sizes=[list(df.online_order).count("Yes"),list(df.online_order).count("No")]
colors=["lightskyblue","lightcoral"]
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',startangle=90,textprops={'fontsize': 14})
plt.title('Online Order option',fontsize=15)
plt.show()


# In[242]:


#count vs ratings for rest. with online order option
dfoo=pd.DataFrame(df[df["online_order"]=="Yes"])

g=sns.countplot(x="ratings",data=dfoo)
g.set_title("Count plot of ratings of restaurants with online order option",fontsize=20,color="blue")
g.set_ylabel("count",fontsize=15,color="green")
g.set_xlabel("ratings",fontsize=15,color="green")
plt.show()


# In[ ]:


#not much of a shift in mean
#online order doesn't have an impact on ratings


# ###########################################################################################################################

# In[102]:


#what % of restaurants have book table option

labels="Yes","No"
sizes=[list(df.book_table).count("Yes"),list(df.book_table).count("No")]
colors=["lightgreen","pink"]
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',startangle=90,textprops={'fontsize': 14})
plt.title('Book Table option',fontsize=15)
plt.show()


# In[251]:


#does book table option being there correspond to higher ratings?
#ideally, it should.

g=sns.countplot(x="ratings",data=df,hue="book_table")
g.set_title("Count plot of ratings of restaurants with/wo book table option",fontsize=20,color="blue")
g.set_ylabel("count",fontsize=15,color="green")
g.set_xlabel("ratings",fontsize=15,color="green")
#g.set(xlim=(2.2,4.9),ylim=(0,140))
plt.show()


# In[ ]:


#mean has shifted
#ie, restaurants with book table option tend to have a higher mean rating


# #############################################################################################################################

# In[110]:


#top 10 locations with the most number of restaurants

g=sns.countplot(x="city_specifics", data=df, palette="hls",
              order=df.city_specifics.value_counts().iloc[:10].index)
g.set_title("Top ten locations with most number of restaurants",fontsize=20,color="red")
g.set_xlabel("Location",fontsize=15,color="green")
g.set_ylabel("Count",fontsize=15,color="green")
g.set_xticklabels(g.get_xticklabels(), rotation=40, ha="right")
for p in g.patches:
    g.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')
plt.show()


# In[34]:


#Whitefield has the most no of rest. 


# In[296]:


cuisine_list=[]
for i,j in df['cuisines'].iteritems():
    if df["city_specifics"].loc[i]=="Whitefield":
        c_arr=j.split(",")
        for item in c_arr:
            cuisine_list.append(item.lstrip())

data={"cuisines":cuisine_list}
dfcw=pd.DataFrame(data)

g=sns.countplot(x="cuisines",data=dfcw, palette="Set1",order=dfcw.cuisines.value_counts().iloc[:10].index)
g.set_title("Different cuisines in Whitefield",fontsize=20,color="blue")
g.set_xlabel("Cuisine",fontsize=15,color="green")
g.set_ylabel("Count",fontsize=15,color="green")
g.set_xticklabels(g.get_xticklabels(), rotation=40, ha="right")
for p in g.patches:
    g.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')
plt.show()


# ############################################################################################################################

# In[192]:


#which cuisine is more popular(in terms of number)?
#top ten cuisines

#one restaurant may have more than one cuisine, have to take care of that
cuisine_list=[]
for i,j in df['cuisines'].iteritems():
        c_arr=j.split(",")
        for item in c_arr:
            cuisine_list.append(item.lstrip())

data={"cuisines":cuisine_list}
dfc=pd.DataFrame(data)

g=sns.countplot(x="cuisines",data=dfc, palette="Set1",order=dfc.cuisines.value_counts().iloc[:10].index)
g.set_title("Top ten most popular cuisines in terms of number",fontsize=20,color="blue")
g.set_xlabel("Cuisine",fontsize=15,color="green")
g.set_ylabel("Count",fontsize=15,color="green")
g.set_xticklabels(g.get_xticklabels(), rotation=40, ha="right")
for p in g.patches:
    g.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')
plt.show()


# In[32]:


#the most popular cuisine is North Indian


# ##########################################################################################################################

# In[164]:


#what are the largest restaurant chains?

g=sns.countplot(x="name",data=df, palette="hls",order=df.name.value_counts().iloc[:10].index)
g.set_xlabel("Restaurant chain name",fontsize=15,color="green")
g.set_ylabel("Count",fontsize=15,color="green")
g.set_title("G*     Top 10 largest restaurant chains(with most branches)",fontsize=20,color="hotpink")
g.set_xticklabels(g.get_xticklabels(), rotation=40, ha="right")

for p in g.patches:
    g.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')


# In[89]:


#Cafe Coffee Day is the largest chain


# In[165]:


#CCD has the most number of restaurants. Does this also mean it has the highest rating?
#checking to see if no. of branches affects rating in any way

g=sns.countplot(x="name",data=df, palette="Set3",order=df[df["ratings"]>=4.5]["name"].value_counts().iloc[:10].index)
g.set_xlabel("Restaurant chain name",fontsize=15,color="green")
g.set_ylabel("Count",fontsize=15,color="green")
g.set_title("G**     Top 10 restaurant chains(with most branches, where ratings>4.5)",fontsize=20,color="orange")
g.set_xticklabels(g.get_xticklabels(), rotation=40, ha="right")

for p in g.patches:
    g.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')


# In[ ]:


#we see that none of the names in G* appear in G**. 
#This means that all the rest. in G** have higher ratings than the ones in G*
#There are restaurants with less no. of branches, but higher rating.
#ex- Pasta Street, which has only 3 branches, has a higher rating than CCD, which has 49 branches


# ############################################################################################################################

# In[176]:


#ratings and votes
x=np.array(df["votes"])
y=np.array(df["ratings"])
g=sns.scatterplot(x,y,data=df)
g.set_xlabel("Votes",color="green",fontsize=15)
g.set_ylabel("Ratings",color="green",fontsize=15)
g.set_title("Ratings vs. Votes",color="red",fontsize=20)
plt.show()


# In[ ]:


#low rated restaurants(<3.5) do not have more than 1500 votes
#most restaurants with higher ratings have votes lying bw 0-2500


# In[177]:


#what is the one outlier in the top right corner?
#it seems to have a high rating and a great number of votes


# In[180]:


df.sort_values(by=['votes'],ascending=False)


# In[181]:


#the outlier is 'Byg Brewski Brewing Company'
#followed by Toit and Truffles
#what makes these restaurants so popular?


# In[ ]:


#if we look at the column 'city_specifics', we can see that the really popular restaurants(votes>10000),
#are located in IT/Business hubs(Bellandur, Indiranagar, Marathahalli, Koramangala)

#we can also see that the restaurant types of these places are perfect for office lunches


# ##############################################################################################################################

# In[189]:


#rating vs meal type

g=sns.barplot(x="meal_type",y="ratings",data=df)
g.set_xlabel("meal type",color="green",fontsize=15)
g.set_ylabel("ratings",color="green",fontsize=15)
g.set_title("Ratings vs. Meal type",color="red",fontsize=20)
plt.show()


# In[288]:


#why is 'Drinks & nightlife' varying so much in ratings
for i,j in df["meal_type"].iteritems():
    if j=="Drinks & nightlife":
        print(df["city_specifics"].loc[i])      


# ***************************

# In[ ]:




