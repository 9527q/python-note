#!/usr/bin/env python
# coding: utf-8

# # pandas

# In[1]:


import pandas as pd
import numpy as np


# In[6]:


df = pd.DataFrame(pd.read_csv('query.csv', header=0))
df = pd.DataFrame(pd.read_excel('query.csv'))


# In[8]:


type(pd.read_csv('query.csv', header=0))


# In[ ]:




