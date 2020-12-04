#!/usr/bin/env python
# coding: utf-8

# In[16]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import sqlalchemy
from datetime import date


# In[17]:


engine=sqlalchemy.create_engine('mysql+pymysql://root:night@97@localhost:3306/tatasteel')


# In[18]:


df=pd.read_sql_table('challan',engine)

df


# In[19]:



df['memocycle'] = (df.memoapprovedate-df.memocreatedate).astype('timedelta64[h]')
df['chalancycle'] = (df.challan_appdate - df.memoapprovedate).astype('timedelta64[h]')
df['SEScycle'] = (df.SES_appdate - df.challan_appdate).astype('timedelta64[h]')
df


# In[20]:


month=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
xpos=np.arange(len(month))
frequency=np.zeros(12)
for i in range(1,13):
    count=0
    for row in df.memoapprovedate:
        if row.month==i:
            count+=1
    frequency[i-1]=count
    
frequency


# In[21]:


plt.xticks(xpos,month)
plt.ylabel('FREQUENCY')
plt.title('MEMO_APP_FRQCYCLE')
plt.bar(xpos,frequency,color='red',label='frequency')
plt.legend(loc='best')


# In[41]:


month=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
xpos=np.arange(len(month))
frequency=np.zeros(12)
for i in range(1,13):
    count=0
    for row in df.challan_appdate:
        if row.month==i:
            count+=1
    frequency[i-1]=count
plt.figure(figsize=(6,4))
plt.xticks(xpos,month)
plt.ylabel('FREQUENCY')
plt.title('CHALLAN_APP_FRQCYCLE')
plt.bar(xpos,frequency,color='yellow',label='frequency')
plt.legend(loc='best')


# In[10]:


month=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
xpos=np.arange(len(month))
frequency=np.zeros(12)
for i in range(1,13):
    count=0
    for row in df.SES_appdate:
        if row.month==i:
            count+=1
    frequency[i-1]=count
    
plt.xticks(xpos,month)
plt.ylabel('FREQUENCY')
plt.title('SES_APP_FRQCYCLE')
plt.bar(xpos,frequency,color='orange',label='frequency')
plt.legend(loc='best')


# In[42]:


quater=['1ST QUATER','2ND QUATER','3RD QUATER','4TH QUATER']
xpos=np.arange(len(quater))
frequency1=np.zeros(4)
frequency2=np.zeros(4)
frequency3=np.zeros(4)

count1=np.zeros(12)
count2=np.zeros(12)
count3=np.zeros(12)


for row in df.memoapprovedate:
    count1[row.month-1]+=1
c=0
for i in range(0,4):
    for j in range(c,c+3):
        frequency1[i]=frequency1[i]+count1[j]
    c+=3
    

    
for row in df.challan_appdate:
    count2[row.month-1]+=1
c=0
for i in range(0,4):
    for j in range(c,c+3):
        frequency2[i]=frequency2[i]+count2[j]
    c+=3
    

    
for row in df.SES_appdate:
    count3[row.month-1]+=1
c=0
for i in range(0,4):
    for j in range(c,c+3):
        frequency3[i]=frequency3[i]+count3[j]
    c+=3
    

xpos=np.arange(len(quater))
plt.xticks(xpos,quater)
plt.ylabel('FREQUENCY')
plt.title('FINANCIAL YEAR')
plt.bar(xpos-0.3,frequency1,width=0.3,color='RED',label='MEMOAPPDATE')
plt.bar(xpos+0,frequency2,width=0.3,color='ORANGE',label='CHALLAN_APPDATE')
plt.bar(xpos+0.3,frequency3,width=0.3,color='BLUE',label='SES_APPDATE')
plt.legend(loc='best')


# In[11]:


f=pd.DataFrame(df,index=None,columns=['memocycle','chalancycle','SEScycle'])
cycle=['MEMOCYCLE','CHALANCYCLE','SESCYCLE']
time=[f['memocycle'].mean(),f['chalancycle'].mean(),f['SEScycle'].mean()]
xpos=np.arange(len(cycle))
plt.xticks(xpos,cycle)
plt.ylabel('TIME(in hrs)')
plt.title('AVGCYCLE')
plt.bar(xpos+0.2,time,width=0.6,color='purple',label='AVG')
plt.legend(loc='best')


# In[12]:


f.max(axis=1,)


# In[13]:


df['sum']=df['memocycle']+df['chalancycle']+df['SEScycle']
df


# In[14]:



df[df['sum']==df['sum'].max()]


# In[15]:


df[df['sum']==df['sum'].min()]


# In[ ]:




