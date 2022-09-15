#!/usr/bin/env python
# coding: utf-8
1. [] is an empty set.
# In[2]:


spam = [2, 4, 6, 8, 10]


# In[3]:


spam [2] = 'Hello'


# In[4]:


spam


# In[5]:


spam = ['a', 'b', 'c' , 'd' ]
        


# In[6]:


spam[int(int('3' * 2) / 11)]


# In[7]:


spam[-1]


# In[8]:


spam[:2]


# In[9]:


bacon = [3.14 , 'cat' , 11, 'cat' , True]


# In[10]:


bacon.index('cat')


# In[11]:


bacon.append(99)


# In[12]:


bacon


# In[13]:


bacon.remove('cat')


# In[14]:


bacon

list concatination operator = +
list replication operator = *

Append adds the number or the item at the end and insert adds it at the assigned index no.

The two methods to remove are .pop and .remove function.


The similarities are as follows:
- Both lists and strings can be passed to len()
- Have indexes and slices
- Can be used in for loops
- Can be concatenated or replicated
- Can be used with the in and not in operators

Lists : are mutable - they can have values added, removed, or changed. lists use the square brackets, [ and ]
Tuples : are immutable; they cannot be changed at all. Tuples are written using parentheses, ( and )



# In[15]:


tuple = (42,)
tuple


# In[26]:


call tuple


# In[23]:


l1 = [1,2,3,4,5,6,7]


# In[24]:


list = tuple(l1)


# In[32]:


l1 = [2,3]
l = (*l1,)
l


# In[33]:


type(l)


# In[27]:


t1 = (3,4)
t = list(t1)
t


# In[34]:


type(t)


# In[ ]:


List values


# In[ ]:


The copy.copy() function will do a shallow copy of a list,
The copy.deepcopy() function will do a deep copy of a list. only copy.deepcopy() will duplicate any lists inside the list


# In[ ]:




