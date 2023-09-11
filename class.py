#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class FirstClass1:

    def __init__(self, *args):
        self.listv = args[0]

    def fcfirst_method1(self):
        print("fcfirst_method1")
        print(self.listv)
        for vr in self.listv:
            print(vr)

    def fcsecond_method1(self):
        print("fcsecond_method1")


obje1 = FirstClass1([1, 2, 4, 5, 6])

obje1.fcfirst_method1()
obje1.fcsecond_method1()


# In[ ]:


class Vehicle:
    def __init__(self):
        self.engine = '1500cc'

class Car(Vehicle):
    def __init__(self, max_speed):
        # call parent class constructor
        super().__init__()
        self.max_speed = max_speed

    def display(self):
        # access parent class instance variables 'engine'
        print("Engine:", self.engine)
        print("Max Speed:", self.max_speed)

# Object of car
car = Car(240)
car.display()


# In[ ]:





# In[21]:


class Vehicle:
    def __init__(self):
        self._engine = '1500cc'

class Car(Vehicle):
    def __init__(self, max_speed):
        # call parent class constructor
        super().__init__()
        self.max_speed = max_speed

    def display(self):
        # access parent class instance variables 'engine'
        print("Engine:", self._engine)
        print("Max Speed:", self.max_speed)

# Object of car
car = Car(240)
car.display()

