# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:24:05 2020

@author: praja
"""
#
from pattern.en import parse
from pattern.en import pprint
##
pprint(parse('He went to park', relations=True, lemmata=True))
print("sucesfull!!!")

