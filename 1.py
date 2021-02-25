#!/usr/bin/env python
# coding: utf-8

# In[22]:


import jieba
import json


# In[23]:


commentList = open('comments.txt', 'r', encoding='utf-8').read()
print(commentList)


# In[24]:


words = jieba.lcut(commentList)#jieba.cut生成的是一个生成器，generator，也就是可以通过for循环来取里面的每一个词。jieba.lcut 直接生成的就是一个list
#print(words)


# In[25]:


wordCounts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        wordCounts[word] = wordCounts.get(word, 0) + 1
print(wordCounts)


# In[26]:


items = list(wordCounts.items())
items.sort(key=lambda x: x[1], reverse=True)
countList = []
for i in range(len(items)):
    countDict = {}
    word, count = items[i]
    if count >= 10:
        countDict['name'] = word
        countDict['value'] = count
        countList.append(countDict)
#print(countList)


# In[27]:


data = {}
data['data'] = countList
print(data)
with open('comments.json', 'w', encoding='utf-8') as f:
    json.dump(data,f, ensure_ascii=False, indent=4)
    #输出真正的中文需要指定ensure_ascii=False,indent的数值，代表缩进的位数


# In[ ]:




