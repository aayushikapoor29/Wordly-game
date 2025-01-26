#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import requests


# In[46]:


def select_word():
    api_word = "https://api.datamuse.com/words?sp=?????"
    word = random.choice((requests.get(api_word).json()))['word']
    return word


# In[101]:


def wordle():
    attempts = 6
    word = select_word()
    print(word)
    
    status = ["⬜" for i in range(5)]
    while attempts>0:
        guess = input('enter a word: ')
        if len(guess) == 5:
            for i, letter in enumerate(guess):
                if letter == word[i]:
                    status[i] =  "🟩"
                elif letter in word:
                    status[i] = "🟨"
        else:
            print('Length of word is incorrect')
            wordle()
            
        print(' '.join(status))
        
        if ''.join(status) == '🟩'*5:
            print('Yaayaa, you have guessed the correct word')
            n = input('do you want to play more? : (y/n)')
            if n=='y':
                wordle()
            else:
                break
        else:
            attempts -= 1
        status = ["⬜" for i in range(5)]
    if attempts == 0:
        print(f'BOOOOOO!!! you did not come even close\n, the word was {word}')
        n = input('do you want to play more? : (y/n)')
        if n=='y':
                wordle()
        else:
                exit


# In[99]:


wordle()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




