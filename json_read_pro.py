#!/usr/bin/env python
# coding: utf-8

# In[36]:


import json
path = 'E:\GIt\inputdata.json'
with open(path) as data:
      fil_data = data.read()
print(type(fil_data))
read_json = json.loads(fil_data)
print(read_json)
print(type(read_json))


# In[8]:


get_ipython().system('pip install jsonpath-ng')


# In[10]:


from jsonpath_ng import jsonpath, parse


# In[21]:


find_path = parse('$.hobbies')
get_data = find_path.find(read_json)
print(get_data[0].path)
print(get_data[0].value)


# In[25]:


path1 = 'E:\GIt\jsonschema.json'
with open(path1) as data1:
      fil_data1 = data1.read()
print(type(fil_data1))
read_json1 = json.loads(fil_data1)
read_json1


# In[27]:


get_ipython().system('pip install jsonschema')


# In[40]:


import json
import jsonschema
from jsonschema import validate
try:
   validate(instance=read_json, schema=read_json1)
   print(true)
except Exception as err:
    print(err)
else:
    print("some thing wrong")

