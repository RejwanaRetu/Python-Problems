
# coding: utf-8

# In[12]:


ch = "abcdefghijklmnopqrstuvwxyz"
a = str(input('enter a string: '))
for i in ch:
    c = a.count(i)
    if c>1:
        print(i,c)
    
    

