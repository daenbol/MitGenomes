#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import re

#os.chdir("/home/daenbol/Documents/NurProjects/1Pars")
#temp = os.listdir()

file1 = open("scaffolds.fasta", "r")
z = file1.readlines()
file1.close()

e = 0

with open("scaffoldsOFinterest.fasta", "x") as file2:
    for i in z:
        if (">" in i):
            #file2.replace(int(re.search(r'\d+', i).group()), int(re.search(r'\d+', i).group())+1)
            a = re.search(r'length_\d+', i).group()
            b = int(re.search(r'\d+', a).group())
            print(b)
            if (b > 15000) and (b < 17000):
                #file2.write(str(re.search(r'length_\d+', i).group()))
                file2.write(i)
                e = 1
            else:
                e = 0
                next
        else:
            if (e == 1):
                file2.write(i)
                next
            else:
                next


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




