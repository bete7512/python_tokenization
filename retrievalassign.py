#!/usr/bin/python3
'''
1.  TSEGABIZU  TEDLA----------------------------------- 1203187
2.  BETE  GOSHIME---------------------------------------- 1201157
3.  DEJEN  BRIHANU-------------------------------------- 1201413
4.  BEKALU  TENNA--------------------------------------- 1201093
5.  HERMELA  AMEHA------------------------------------ 1201985'''
import nltk
import re
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
text = open('test.txt',"r")
fulltext = text.read()
cleaneddocument=re.sub("[^\w\s]","",fulltext)
print("So basically tokenizing involves splitting sentences is going below")
print("***************************************************************************")
print("***************************************************************************")
print(sent_tokenize(cleaneddocument))
print("***************************************************************************")
print("***************************************************************************")
print("tokenized words with out any removal of articles punctuation")
print("***************************************************************************")
print("***************************************************************************")
print(word_tokenize(cleaneddocument))
print("***************************************************************************")
print("***************************************************************************")
word_tokenized = word_tokenize(cleaneddocument)
from nltk.corpus import stopwords
stop_words=stopwords.words('english')
print("***************************************************************************")
print(stop_words)
print("***************************************************************************")
real_words = []
for word in word_tokenized:
    if word not in stop_words:
        real_words.append(word)
print("***************************************************************************")
print("***************************************************************************")
print("cleaned words from stop words")
print(real_words)
print("***************************************************************************")
print("***************************************************************************")
root_word = []
from nltk.stem import PorterStemmer
rooter=PorterStemmer()
for words in real_words:
    root_word.append(rooter.stem(words))
print("***************************************************************************")
print("***************************************************************************")
print(root_word)
