#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# In[2]:


x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x,y)
plt.xlabel('x', fontsize = 20)
plt.ylabel('y', fontsize = 20)
plt.title('Simple line', fontsize=20)
print("Q1-Answer")


# In[3]:


x = [0, 20, 30]
y1 = [40,0,30]
y = [20, 40, 0]
x1=[0,20,30]
plt.plot(x,y,label='line1')
plt.plot(x1,y1,color='g',label='line1')
plt.xlabel('x', fontsize = 20)
plt.ylabel('y', fontsize = 20)
plt.title('Multiple Line Plot', fontsize=20)
plt.legend()
print("Q2-Answer")


# In[4]:


x = [0, 20, 30]
y1 = [40,0,30]
y = [20, 40, 0]
x1=[0,20,30]
plt.plot(x,y,color='r',label='line1-lw-3',lw=3)
plt.plot(x1,y1,color='b',label='line1-lw-2',lw=2)
plt.xlabel('x', fontsize = 20)
plt.ylabel('y', fontsize = 20)
plt.title('Different widths and colors', fontsize=20)
plt.legend()
print("Q3-Answer")


# In[5]:


x = [0, 20, 30]
y1 = [40,0,30]
y = [20, 40, 0]
x1=[0,20,30]
plt.plot(x,y,color='r',label='line1-dashed',lw=3,linestyle='--')
plt.plot(x1,y1,color='b',label='line1-dotted',lw=2,linestyle=':')
plt.xlabel('x', fontsize = 20)
plt.ylabel('y', fontsize = 20)
plt.title('Different styles. Plot', fontsize=20)
plt.legend()
print("Q4-Answer")


# In[6]:


x = [0, 10, 20,30]
y = [20, 40, 0,40 ]
plt.plot(x,y,color='r',lw=2,linestyle=':',marker='o',mfc='b',mec='b')
plt.xlabel('x', fontsize = 20)
plt.ylabel('y', fontsize = 20)
plt.title('Markers Plot', fontsize=20)
print("Q5-Answer")


# In[7]:


Languages = ['Java','Pyhton','PHP','JavaScript','C#','C++']
popularity = [22.2, 17.6, 8.8,8,7.7,6.7 ]
plt.bar(Languages,popularity)
plt.xlabel('Programming Languages', fontsize = 20)
plt.ylabel('Popularity', fontsize = 20)
plt.title('Popularity of programming Languages', fontsize=20)
print("Q6-Answer")


# In[8]:


Languages = ['Java','Pyhton','PHP','JavaScript','C#','C++']
popularity = [22.2, 17.6, 8.8,8,7.7,6.7 ]
ax= sns.barplot(x=Languages,y=popularity)
ax.set_xlabel('Programming Languages', fontsize = 20)
ax.set_ylabel('Popularity', fontsize = 20)
ax.set_title('Popularity of programming Languages', fontsize=20)
print("Q6-Another-Answer")


# In[9]:


Languages = ['Java','Pyhton','PHP','JavaScript','C#','C++']
popularity  = [22.2, 17.6, 8.8,8,7.7,6.7 ]
plt.barh(Languages,popularity )
plt.ylabel('Programming Languages', fontsize = 20)
plt.xlabel('Popularity', fontsize = 20)
plt.title('Popularity of programming Languages', fontsize=20)
print("Q7-Answer")


# In[10]:


men = [22, 30, 35, 35, 26]
women = [25, 32, 30, 35, 29 ]
df = pd.DataFrame({"Men": men, "Women":women})
ax = df.plot(kind="bar")
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
ax.set_xlabel('Group', fontsize = 20)
ax.set_ylabel('Scores', fontsize = 20)
ax.set_title('Scores by Group and Gender', fontsize = 20)
plt.show
print("Q8-Answer")


# In[11]:


labels=('G1', 'G2', 'G3', 'G4', 'G5')

sex_counts = {
    'Male': np.array( [22, 30, 35, 35, 26]),
    'Female': np.array([25, 32, 30, 35, 29 ]),
}
width = 0.6
fig, ax = plt.subplots()
bottom = np.zeros(len(labels))

for sex, sex_count in sex_counts.items():
    p = ax.bar(labels, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count
    ax.bar_label(p, label_type='center')
    
ax.set_title('Scores by Group and Gender', fontsize = 20)
ax.legend()
plt.show()
print("Q8-Another-Answer")


# In[12]:


languages  = ['Java','Pyhton','PHP','JavaScript','C#','C++']
popularity  = [22.2, 17.6, 8.8,8,7.7,6.7 ]
palette_color = sns.color_palette('bright')
plt.pie(popularity ,labels=languages ,colors=palette_color,autopct='%.0d%%')
plt.show
print("Q9-Answer")

