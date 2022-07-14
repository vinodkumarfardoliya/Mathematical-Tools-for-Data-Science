#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions. 
# 
# You are all required to upload this file on github before 23:59 on 1/6/2022.

# #### Import NumPy as np

# In[1]:


import numpy as np


# #### Create an array of 10 zeros 

# In[2]:


np.zeroes(10)


# #### Create an array of 10 ones

# In[4]:


np.ones(10)


# #### Create an array of 10 fives

# In[7]:


np.ones(10) * 5


# #### Create an array of the integers from 10 to 50

# In[9]:


np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[10]:


np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[11]:


np.arange(0,9).reshape((3,3))


# #### Create a 3x3 identity matrix

# In[13]:


np.eye(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[33]:


np.random.rand(0,1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[34]:


np.random.randn(25)


# #### Create the following matrix:

# In[40]:


np.arange(0.01,1.01,0.01).reshape(10,10)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[41]:


np.linspace(0,1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[64]:


arr=np.arange(1,26).reshape(5,5)


# In[40]:


arr[2:,1:]


# In[41]:


arr[3,4]


# In[42]:


arr[:3,1].reshape(3,1)


# In[54]:


arr[4]


# In[49]:


arr[3:5]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[71]:


arr=np.arrange(1,26)\n
arr.reshape(5,5)\n
arr.sum()


# #### Get the standard deviation of the values in mat

# In[74]:


arr.std()


# #### Get the sum of all the columns in mat

# In[76]:


arr.sum(axis=0)


# # Great Job!
