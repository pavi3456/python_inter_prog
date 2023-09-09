#!/usr/bin/env python
# coding: utf-8

# In[24]:


n1 = "pavithran"
#name[-1:-len(name)-1:-1]
n1 = list(n1)
print(set(n1))


# In[9]:


sort = [8,15,18, 25, 10,11,12,16]
for i in range(len(sort)-1):
    if sort[i] < sort[i+1]:
        continue
    else:
        temp = sort[i]
        temp2 =sort[i+1]
        sort[i+1] = temp
        sort[i] = temp2       
        
print(sort)


# In[25]:


empty = {}
count =1
for i in name:
    if i in empty:
        empty[i] = empty[i]+1
    else:
        empty[i] = count
empty
for value in empty:
    if empty[value] > 1:
        print("%s : occers 2 time" % value)


# In[38]:


a = [8, 15, 18, 10, 11, 12, 16, 25]
a = [i for i in a if i%2==0]
print(a)


# In[39]:


a[0]


# In[42]:


x = lambda x : x+2
x(a[1])


# In[46]:


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    print("next step")
    return inner

@smart_divide
def divide(a, b):
    out = a/b
    return out

output = divide(2,5)
print(output)


# In[62]:


@smart_func
def divide(a, b):
     print(a/b)
    
    
def smart_func(func):
    
    def inner_func(a, b):
        a, b = b, a
        return func(a, b)
    return inner_func
        
divide(5, 10)


# In[133]:


@smart_func2
def divide2():
     print("first1 function")
    
    
def smart_func2(func):
    
    def inner_func2():
        print("second1 function")
        func()
        print("third5 function")
    return inner_func2
        
divide2()


# In[51]:


def smart_divide(func):
    print(a)
    print(b)

@smart_divide
def divide(a, b):
    out = a/b

output = divide(2,5)
print(output)

print("new programe")

