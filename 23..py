
# coding: utf-8

# In[22]:


x = int(input("enter a number: "))
if((x%10 == 0) and (x%50 == 0)):
    if ((x%30 == 0)):
            print('divisible by 10,50,30')
    else:
            print('divisible by 10,50 but not by 30')
else:
    print('divisible by 10 but not 50')

