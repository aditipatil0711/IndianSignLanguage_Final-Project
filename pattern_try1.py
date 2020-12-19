# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:24:05 2020

@author: praja
"""
#
#from pattern.en import parse
#from pattern.en import pprint
##
#pprint(parse('He went to park', relations=True, lemmata=True))
#print("sucesfull!!!")

#
#import spacy
#import textacy
#import en_core_web_sm
#nlp =spacy.load('en_core_web_sm')
#doc = nlp("I am Prajakta. working on NLP project excites me.I like ISL." )
#
#for token in doc:
#    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,)


#
#from polyglot.text import Text 
#sentence = "Hello, myself Prajakta. I am working on python project."
#text = Text(sentence) 
#print(text.pos_tags)

import en_core_web_sm
import spacy
import textacy
nlp = en_core_web_sm.load()
SUBJ = ["nsubj","nsubjpass"] 
VERB = ["ROOT"] 
OBJ = ["dobj", "pobj", "dobj"] 
text = nlp('She played in the park.')
sub_toks = [tok for tok in text if (tok.dep_ in SUBJ) ]
obj_toks = [tok for tok in text if (tok.dep_ in OBJ) ]
vrb_toks = [tok for tok in text if (tok.dep_ in VERB) ]
#text_ext = list(textacy.extract.subject_verb_object_triples(text))
print("Subjects:", sub_toks)
print("VERB :", vrb_toks)
print("OBJECT(s):", obj_toks)
#print ("SVO:", text_ext)