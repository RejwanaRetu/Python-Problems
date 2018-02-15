
# coding: utf-8

# In[17]:


n = int(input('enter a number: '))
if n == 0:
    print('Factorial is: 1')
else:
    fact = n * factorial(n-1)
    print('Factorial is: ',fact)

