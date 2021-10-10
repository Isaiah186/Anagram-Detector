#!/usr/bin/env python
# coding: utf-8

# In[21]:


class Anagrams:
    def __init__(self):
        pass
    
    
    def comparison(self):
        word_one = input("Enter your first word.")
        word_two = input("Enter your second word.")
        
        x = sorted(word_one)
        y = sorted(word_two)
        
        if x==y:
            print("word_one & word_two are both anagrams!")
            
        else:
            print("word_one & word_two are not anagrams!")


# In[22]:


Anagrams_obj = Anagrams()


# In[23]:


Anagrams_obj.comparison()


# In[ ]:




