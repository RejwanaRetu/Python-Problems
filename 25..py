
# coding: utf-8

# In[3]:


Number = int(input("Please Enter the Range Number: "))
i = 0
First_Value = 0
Second_Value = 1
while(i < Number):
           if(i <= 1):
                      Next = i
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next)
           i = i + 1

