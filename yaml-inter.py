#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pyyaml')


# In[21]:


import yaml
from yaml.loader import SafeLoader
with open('E:\GIt\yaml_data.yml') as yamldata:
     data = yaml.load(yamldata, Loader=SafeLoader)
print(data)


# In[22]:


import re


# In[27]:


ip = '192.168.151.99'

pattern = '([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})'

if re.search(pattern, ip):
    print("pattern match")
else:
    print("pattern not match")


# In[34]:


string = '45pavi57890'
num = []
cha = []
for ch in string:
    if ch.isalpha():
        print(ch)
        cha.append(ch) 
    else:
        num.append(ch)
print(''.join(num))
print(''.join(cha))


# In[44]:


name = 'pavibas33@@gmail.com'
spe = ['@', '#', '%']
count = 0
for ch in name:
    if ch in spe:
        count=count+1 
    else:
        continue
print(count)


if condition1:
    # code block 1

elif condition2:
    # code block 2

else: 
    # code block 3
