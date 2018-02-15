
# coding: utf-8

# In[6]:


str = input('enter a string: ')
vowel = "AEIOUaeiou"
consonent = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
countV = 0;
countC = 0;
for i in str:
    if i in vowel:
        countV += 1
    elif i in consonent:
        countC += 1
print("The number of Vowels is: ",countV,"\nThe number of consonents is: ",countC)

