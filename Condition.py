#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
#area=input("Enter the area")


# In[4]:


#type(area)


# In[15]:


area=float(input("Enter the area"))


# In[16]:


type(area)


# In[18]:


if area>0:
    radius=math.sqrt(area/math.pi)
    print("the radius is", radius)
else:
    print("Enter positive number")


# In[21]:


if radius>5:
    diameter=2*radius
    print("diameter is", diameter)
elif radius>4:
    print("you are in elif")
else:
    print("Error")


# ### for loop

# In[34]:


for i in range(1,4):
    print("Hello")


# In[35]:


range(i)


# ### while loop

# In[37]:


counter=5
while counter>1:
    print(counter)
    counter=counter-1


# In[ ]:




