
# coding: utf-8

# In[11]:


name = "xue"


# In[2]:


age = 100


# In[12]:


print (name)


# In[9]:


print (age)


# In[13]:


print ("my name is", name)


# In[15]:


print ("my name is", name, "my age is", age)


# In[16]:


newage= age-60


# In[17]:


multiple=age*2


# In[18]:


print("your age is actually", newage)


# In[19]:


print ("your multiple age is", multiple)


# In[20]:


NewAge =100


# In[21]:


newage =50


# In[22]:


sequence =""


# In[23]:


print (sequence)


# In[24]:


print(sequence [0])


# In[27]:


print(sequence [3])


# In[28]:


print ("my fourth letter is", sequence [3])


# In[29]:


len (sequence)


# In[30]:


print ("the length of the sequence is", len (sequence))


# In[31]:


print (sequence [0:2])


# In[32]:


print (sequence[0:3])


# In[33]:


type (sequence)


# In[34]:


type (100)


# In[35]:


type ("100")


# In[51]:


cox1 = "ATCG"


# In[52]:


cox2 = "GATC"


# In[53]:


cox1 + cox2


# In[48]:


firstname = "xue"


# In[49]:


lastname = "guo"


# In[50]:


firstname + " "+ lastname


# In[45]:


name


# In[46]:


age


# In[47]:


name + age


# In[54]:


5**2


# In[55]:


5*2


# In[56]:


print ("5 sequare is", 5**2)


# In[57]:


5%2


# In[58]:


max (23, 4,5)


# In[59]:


round(3.1415926)


# In[60]:


round(3.1415926,2)


# In[61]:


min (2,5,9)


# In[62]:


help(round)


# In[63]:


max(21,22,45)


# In[64]:


min(21,22,45)


# In[65]:


max(21,22,45)+min(21,22,45)


# In[71]:


hundred_c="c"*50

print (hundred_c)
# In[69]:


hundred_c+cox1


# In[73]:


len (hundred_c + cox1)


# In[74]:


import math


# In[75]:


math.log(2)


# In[76]:


math.pi


# In[77]:


help (math)


# In[79]:


import math
math.cos(45)


# In[80]:


from math import degrees,pi


# In[82]:


angle= degrees (pi/2)


# In[83]:


print (angle)


# In[84]:


import pandas


# In[85]:


pandas.read_csv("data/gapminder_gdp_oceania.csv")


# In[86]:


pandas.read_csv("data/gapminder_gdp_americas.csv")


# In[89]:


data1= pandas.read_csv("data/gapminder_gdp_oceania.csv",index_col="country")


# In[90]:


data1


# In[96]:


data1.T


# In[97]:


data1.describe()


# In[98]:


data1.T.describe()


# In[105]:


data2=pandas.read_csv("data/gapminder_gdp_americas.csv",index_col="country")


# In[101]:


data2


# In[102]:


data2.T


# In[107]:


data2.describe()


# In[109]:


data2.T.describe()


# In[111]:


data2.columns


# In[112]:


data1


# In[113]:


data1.iloc[1,2]


# In[114]:


data1.loc["Australia", "gdpPercap_1962"]


# In[115]:


data1.loc["Australia",:]


# In[117]:


data1.loc[:, "gdpPercap_1962"]


# In[120]:


data1.loc["Australia", "gdpPercap_1952":"gdpPercap_1962"]


# In[122]:


max (data1.loc["Australia","gdpPercap_1952":"gdpPercap_1967"])


# In[132]:


subset=data1.loc[:, "gdpPercap_1952":"gdpPercap_1969"]


# In[133]:


subset[subset>11000]


# In[137]:


data3=pandas.read_csv("data/gapminder_gdp_europe.csv",index_col="country")


# In[135]:


data3


# In[138]:


data3.loc["Serbia","gdpPercap_2007"]


# In[139]:


subset=data3.loc["Italy":"Norway","gdpPercap_1962":"gdpPercap_1972"]


# In[141]:


subset[subset<15000]


# In[143]:


subset.describe()

