#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hola")


# In[3]:


import numpy as np


# In[13]:


#Crear un arreglo ndarray lleno de zeros 

ceros=np.zeros(30)

ceros


# unos=np.ones((5,5))
# 
# unos

# # Crear NDARRA con datos aleatorios
# 

# aleatorio=np.random.rand(5,5
# 
# aleatorio

# In[7]:


aleatorio=np.random.rand(5,5)

aleatorio


# Operaciones con Ndrrays
# 

# In[9]:


suma=np.sum(aleatorio)
suma


# In[10]:


media=np.mean(aleatorio)
media


# In[11]:


mediana=np.median(aleatorio)
mediana


# In[12]:


desviacion=np.std(aleatorio)
desviacion


# In[14]:


seno=np.sin(aleatorio)
seno


# In[15]:


ordenado=np.sort(aleatorio)
ordenado


# #DATOS ESPACIALES
# Un dato espacial es aquel que puede ser asociado a una posicion en el espacio.
# Ya sea en un plano 2D,3D,4D

# In[17]:


import matplotlib.pyplot as plt

#simular uin conjunto de datos que representen la elevación puntual en unn terreno

#Crear un conjunto de datos de prueba
elevacion=np.random.randint(0,3000,size=(100,100))
elevacion


# In[19]:


plt.imshow(elevacion,cmap="terrain")
plt.colorbar(label="Altura(m)")
plt.show()


# In[ ]:




