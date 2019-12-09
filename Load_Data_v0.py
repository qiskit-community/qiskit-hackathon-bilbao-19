#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qiskit


# Gestión de series temporales con método clásico y computación cuántica

# In[8]:


import os
import numpy as np
from sklearn import datasets
from sklearn import tree
import pandas as pd

#Cargamos los datos
os.chdir(r"D:\DeptIA\congresos\cuantica")
data = pd.read_csv("DAX_PERFORMANCE_INDEX.csv", sep=';')
#Creamos un  dataset sin label para el no supervisado
# El primer paso es conocer nuestros datos.
# Realizamos una primera visualizacion.
# EL objetivo es precedir la dureza del cemento.
print(data)

# Visualizamos los 10 primero datos, de una manera mas comoda.
data.head(n=10)


# Normalizamos los datos

# In[9]:


#Creamos una pca
#primero estandarizamos los datos
# Standardizing the features
from sklearn.preprocessing import StandardScaler
x = StandardScaler().fit_transform(data)


# In[10]:





# In[ ]:




