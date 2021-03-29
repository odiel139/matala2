# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 19:18:55 2021

@author: odiel
"""

def revword(word:str):
    little_word=word.lower()
    good_word=little_word[::-1]
    return good_word


def countword():
    count=0
    hendle=open('text.txt')
    line=0
    for x in hendle:
        x=x.rstrip()
        if line==0:
            word=x.lower()
            count=count+1
        if line>0:
            for wordd in x.split():
                sofi_word=revword(wordd)
                if sofi_word==word:
                    count=count+1
        line=line+1            
    return count 

