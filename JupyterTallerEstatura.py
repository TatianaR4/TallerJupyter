#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[5]:


lista_altura=((1.88,1.60,1.60,1.60,1.60,1.60,1.60),(1.65,1.59,1.75,1.59,1.72,1.74,1.80))
altura=np.array(lista_altura)
altura


# In[7]:


media=np.mean(lista_altura)
media


# In[8]:


mediana=np.median(lista_altura)
mediana


# In[9]:


desviacion=np.std(lista_altura)
desviacion


# In[17]:


import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1) # two rows, one column, first plot
plt.imshow(lista_altura,cmap="terrain")
plt.colorbar(label="data")
plt.show()


# In[ ]:





# In[ ]:




