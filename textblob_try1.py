# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:53:09 2020

@author: praja
"""

from textblob import TextBlob
blob= TextBlob("Welcome home mom")
for word, tag in blob.tags:
    print(word,tag)