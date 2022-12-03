#!/usr/bin/env python
# coding: utf-8

# In[1]:


from arcgis.gis import GIS
gis = GIS('https://arcportal-ucop-corps.usace.army.mil/s0portal',verify_cert=False)


# In[2]:


import pandas as pd


# In[3]:


users = gis.users.search(max_users=14000)


# In[4]:


m3users=[acc for acc in users if (acc.username.startswith('m3') or acc.username.startswith('M3'))]


# In[5]:


m3users[0]


# In[20]:


df = pd.DataFrame(columns = ['username','name'])


# In[21]:


for u in m3users:
    df2={'username': u.username, 'name': ' '.join( [w for w in u.fullName.split() if (len(w)>1 and w[1] !='3')])}
    df = df.append(df2, ignore_index = True)


# In[12]:


df.to_csv(r'D:\m3_ucop_users.csv')


# In[7]:


df = pd.read_excel(r"D:\LRN_IPASS Bulk Account Creation Request.xlsx") # can also index sheet by name or fetch all sheets
emaillist = df['Customers Email Address'].tolist()
df2 = pd.read_excel(r'D:\NWO_IPASS Bulk Account Creation Request.xlsx') # can also index sheet by name or fetch all sheets
emaillist2 = df2['Customers Email Address'].tolist()
df3 = pd.read_excel(r"D:\SWL Blue Roof PRT - FMS .xlsx") # can also index sheet by name or fetch all sheets
emaillist3 = df3['Customers Email Address'].tolist()
df4 = pd.read_excel(r'D:\Copy of BlueRoof_PRT_IPASS.xlsx') # can also index sheet by name or fetch all sheets
emaillist4 = df4['Customers Email Address'].tolist()
emails = emaillist + emaillist2+emaillist3 + emaillist4



# In[8]:


for i in range(len(emails)):
    try:
        emails[i] = emails[i].lower()
    except:
        pass


# In[9]:


userids = {}


# In[18]:


for user in m3users:
    if user.role == 'iAAAAAAAAAAAAAAA':
        print(user.fullName)


# In[12]:


userids


# In[20]:


spread = pd.concat([df,df2,df3,df4])
userids['william.g.thomas@usace.army.mil']


# In[24]:


for index, row in spread.iterrows():
    try:
        spread.at[index,'USACE U-PASS ID'] = userids[row['Customers Email Address'].lower()]
        print(row['Customers Email Address'].lower())
    except Exception as e:
        print(e)


# In[23]:


df.to_csv(r'D:\upassids.csv')


# In[28]:


spread


# In[18]:


len(userids)


# In[22]:


df


# In[ ]:




