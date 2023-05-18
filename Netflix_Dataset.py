#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import seaborn as sns


# In[21]:


data=pd.read_csv(r'C:\Users\Dell\Downloads\Netflix Dataset.csv')


# In[22]:


data


# In[23]:


data.info()


# In[24]:


#Task. 1) Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.


# In[25]:


data[data.duplicated()]


# In[26]:


data.drop_duplicates(inplace=True)


# In[27]:


#Task. 2) Is there any Null Value present in any column ? Show with Heat-map.


# In[28]:


data.isnull().sum()


# In[29]:


sns.heatmap(data.isnull())


# In[30]:


#Q. 1) For 'House of Cards', what is the Show Id and Who is the Director of this show ?


# In[31]:


data.head()


# In[33]:


data[data['Title'].isin(['House of Cards'])]   #answer 1


# In[36]:


data[data['Title'].str.contains('House of Cards')]    #answer 2


# In[ ]:





# In[37]:


#Q. 2) In which year the highest number of the TV Shows & Movies were released ? Show with Bar Graph.


# In[38]:


data.head()


# In[62]:


data.dtypes


# In[53]:


data['Release_Date']=pd.to_datetime(data['Release_Date'])


# In[54]:


data.head()


# In[56]:


data['Release_Date'].dt.year.value_counts() #answer


# In[63]:


data['Release_Date'].dt.year.value_counts().plot(kind='bar') #answer


# In[ ]:





# In[64]:


#Q. 3) How many Movies & TV Shows are in the dataset ? Show with Bar Graph.


# In[66]:


data.head()


# In[69]:


data.groupby('Category').Category.count()  #answer 


# In[70]:


data.groupby('Category').Category.count().plot(kind='bar')   #answer


# In[74]:


#Q. 4) Show all the Movies that were released in year 2020.


# In[75]:


data.head()


# In[78]:


data['Year']=data['Release_Date'].dt.year


# In[79]:


data


# In[83]:


data[(data['Category']=='Movie')  & (data['Year']==2020)]   #answer


# In[ ]:





# In[ ]:


#Q. 5) Show only the Titles of all TV Shows that were released in Egypt only.


# In[92]:


data[(data['Category']=='TV Show')  & (data['Country']=='Egypt')] ['Title']   #answer


# In[ ]:





# In[ ]:


#Q. 6) Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?


# In[94]:


data.head()


# In[99]:


data['Director'].value_counts().head(10)   #answer


# In[100]:


#Q. 7) Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".


# In[102]:


data.head(2)


# In[106]:


data[(data['Category']=='Movie')&((data['Type']=='Comedies')|(data['Country']=='United Kingdom'))]


# In[ ]:


#Q. 8) In how many movies/shows, Tom Cruise was cast ?


# In[113]:


data[data['Cast']=='Tom Cruise']


# In[112]:


data[data['Cast'].str.contains('Tom Cruise')]  #error bec null values


# In[114]:


data_new=data.dropna()


# In[116]:


data_new


# In[117]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]   #answer


# In[118]:


#Q. 9) What are the different Ratings defined by Netflix ?


# In[119]:


data['Rating'].unique()  #answer


# In[120]:


data['Rating'].nunique()


# In[121]:


#Q. 9.1) How many Movies got the 'TV-14' rating, in Canada ?


# In[132]:


data[(data['Category']=='Movie') & (data['Rating']=='TV-14') & (data['Country']=='Canada')].shape   #answer


# In[133]:


#Q. 9.2) How many TV Shows got the 'R' rating, after year 2018 ?


# In[139]:


data[(data['Category']=='TV Show')&(data['Rating']=='R')&(data['Year']>2018)]   #answer


# In[140]:


#Q. 10) What is the maximum duration of a Movie/Show on Netflix ?


# In[142]:


data['Duration'].unique()


# In[143]:


data[['Minutes','Units']]=data['Duration'].str.split(' ',expand=True)


# In[144]:


data


# In[145]:


data['Minutes'].max()  #answer


# In[146]:


data['Minutes'].min()


# In[147]:


#Q. 11) Which individual country has the Highest No. of TV Shows ?


# In[148]:


data_TVshow=data[data['Category']=='TV Show']


# In[150]:


data_TVshow.head()


# In[151]:


data_TVshow['Country'].value_counts()


# In[152]:


data_TVshow['Country'].value_counts().head(1)  #answer


# In[153]:


#Q. 12) How can we sort the dataset by Year ?


# In[155]:


data.sort_values(by='Year',ascending=False)  #answer


# In[156]:


#Q. 13) Find all the instances where: Category is 'Movie' and Type is 'Dramas' or Category is 'TV Show' & Type is 'Kids' TV'.


# In[163]:


data[((data['Category']=='Movie')&(data['Type']=='Dramas'))|((data['Category']=='TV Show')&(data['Type']=="Kids' TV"))]


# In[ ]:




