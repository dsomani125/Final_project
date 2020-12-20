# -*- coding: utf-8 -*-
"""Sherlock Holmes_final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_c9J_sX5cRPEw-JZZlJgZWbxWoW4G_t7

In this project we have chose two texts **T1** and **T2**, namely, **"The Hounds of Baskerville", by Sir Arthur Conan Doyle** and **"Pride and Prejudice", by Jane Austen** respectively, on which we perform **simple text pre-processing steps** and **tokenization**. We aim to analyze the frequency distribution of tokens in T1 and T2 separately, and represent them via pictorial means using the **word cloud**. Finally we evaluate the relationship between the word length and frequency for both T1 and T2.
"""

import nltk
nltk.download('punkt')
nltk.download('wordnet')

from urllib.request import urlopen
url1 = "http://gutenberg.org/files/2852/2852-0.txt"
url2 = "http://gutenberg.org/files/1342/1342-0.txt"
t1 = urlopen(url1).read()
t2 = urlopen(url2).read()

print(type(t1))
len(t1)

print(type(t2))
len(t2)

t1[:100]

t2[:100]

rawbook1 = t1.decode('utf-8')
rawbook2 = t2.decode('utf-8')

print(type(rawbook1))
print(type(rawbook2))

"""**Data Cleaning of text T1 and T2**

"""

rawbook1_line_list = rawbook1.splitlines()

rawbook2_line_list = rawbook2.splitlines()

"""In the following code block we find out the line number from the start, where the extra text before the Chapter 1 of novel (**t1**) ends.
Similarly we find out the line number for **t1** where the last chapter of novel ends, so that extra unwanted text after that can be removed.
"""

start_index = 0
end_index = 0

for line in rawbook1_line_list[0:]:
  if line == "Chapter 1.":
     print(start_index)
  if line == "THE END":
     print(end_index)
     break
  start_index += 1
  end_index += 1

"""As done above for t1, we do the same for **t2**, and find out **start_index**: the line where extra text before starting of Chapter 1 of novel ends, and **end_index**: the line where the last chapter of novel ends."""

start_index = 0;
end_index = 0;
for line in rawbook2_line_list[0:]:
  if line == "      Chapter 1":
     print(start_index)
  if line == "End of the Project Gutenberg EBook of Pride and Prejudice, by Jane Austen":
     print(end_index)
     break
  start_index += 1
  end_index +=1

"""> **Data Cleaning of T1**



**Removing unwanted text and chapter headings for T1**

In the following code block we aim to make preparation for removing the headings "Chapter i." from text **T1** for every ith chapter.
For that we make a chapter_list conatining all the chapter names by using regular expression, as every chapter heading in the contents section follows a same pattern.
"""

import regex as re
chapter_list = []
pattern = r' Chapter [0-9][0-9]?'
for line in rawbook1_line_list[:88]:
   if bool(re.search(pattern, line)):
     line = re.sub("\t",".",line)
     temp_line = line[1:]
     chapter_list.append(temp_line)
print(chapter_list)

"""In the following block of code we obtain **raw_list1**, which contains text of **t1** without the unwanted text i.e removal of running section, and then we convert the **list raw_list1 into string joined_book1** using join function, replacing all the tab spaces with the single space."""

raw_list1 = rawbook1_line_list[89:7369]
joined_book1 = ''.join(raw_list1)
joined_book1 = joined_book1.replace('      ',' ')
joined_book1

"""In the code block below we have used items of chapter_list (which contains all the chapter headings of **T1**) as a parameter for **sub()** function, to remove all the chapter headings from the joined_book1."""

for item in chapter_list:
  joined_book1 = re.sub(item,"",joined_book1)
joined_book1 = joined_book1[1:]
joined_book1

"""> **Data cleaning of T2**

**Removing unwanted text and chapter headings from text T2**

In the following code block we remove the unwanted text from **T2** and then convert the **list rawbook2_line_list into a string joined_book2** containing the required text of **T2** by using the **join()** function. And finally we further clean the text data by replacing tab spaces with single spaces using **replace()** function.
"""

raw_list2 = rawbook2_line_list[167:14227]
joined_book2 = ''.join(raw_list2)
joined_book2 = joined_book2.replace('      ',' ')
joined_book2

"""Now we remove the headings "Chapter i" present in **T2** before every ith chapter, by using **sub(old,new,string)** function, in which a regular expression corresponding to the heading pattern has been passed as old parameter in sub function."""

import regex as re

pattern = r'Chapter [0-9][0-9]?'
joined_book2 = re.sub(pattern,"",joined_book2)
joined_book2 = joined_book2[2:]
joined_book2

""">    **Tokenizing T1 and T2**

We have used **tokenize.word_tokenize()** method to extract the tokens from the strings T1 and T2.
"""

tokens_t1 = nltk.word_tokenize(joined_book1)
tokens_t2 = nltk.word_tokenize(joined_book2)

type(tokens_t1)
type(tokens_t2)

print("Length of tokens_t1:" + str(len(tokens_t1)))
print("Length of tokens_t2:" + str(len(tokens_t2)))

tokens_t1[:10]

tokens_t2[:10]

"""

> **Analyze the frequency distribution of tokens in T1 and T2 separately**

"""

import pandas as pd

token_series_t1 = pd.Series(tokens_t1)
token_series_t2 = pd.Series(tokens_t2)

"""**Frequency distribution of T1**"""

freq_dist_t1 = token_series_t1.value_counts()
print(type(freq_dist_t1))
freq_dist_t1

"""We can observe the most frequently occuring tokens of **t1** from the following frequency distribution dictionary (**freq_dist_dict_t1**)."""

freq_dist_dict_t1 = dict(freq_dist_t1)
freq_dist_dict_t1

"""**Frequency distribution of T2**"""

freq_dist_t2 = token_series_t2.value_counts()
print(type(freq_dist_t2))
freq_dist_t2

"""We can observe the most frequently occuring tokens of **t1** from the following frequency distribution dictionary (**freq_dist_dict_t2**)."""

freq_dist_dict_t2 = dict(freq_dist_t2)
freq_dist_dict_t2

"""

>  **Creating Word Cloud for T1 and T2.**

"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt

"""**T1's** **Word** **Cloud**"""

comment_words_t1 = ''
for i in range(len(tokens_t1)): 
  tokens_t1[i] = tokens_t1[i].lower() 
      
comment_words_t1 += " ".join(tokens_t1)+" "

wordcloud_t1 = WordCloud(width = 800, height = 800, 
                background_color ='black', 
                min_font_size = 10 , stopwords={','}).generate(comment_words_t1)

plt.figure(figsize = (8, 8), facecolor = 'green') 
plt.imshow(wordcloud_t1) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show()

"""**T2's Word Cloud**"""

comment_words_t2 = ''
for i in range(len(tokens_t2)): 
  tokens_t2[i] = tokens_t2[i].lower() 
      
comment_words_t2 += " ".join(tokens_t2)+" "

wordcloud_t2 = WordCloud(width = 800, height = 800, 
                background_color ='black', 
                min_font_size = 10 , stopwords={','}).generate(comment_words_t2)

plt.figure(figsize = (8, 8), facecolor = 'green') 
plt.imshow(wordcloud_t2) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show()

"""


> **Removing stopwords from T1 and T2 and generating Word Cloud for each again.**



"""

nltk.download('stopwords')

from nltk.corpus import stopwords
all_stopwords = stopwords.words('english')

"""**Word Cloud for T1 after removing stopwords.**"""

wordcloud_sw_t1 = WordCloud(width = 800, height = 800, 
                background_color ='black', 
                stopwords = all_stopwords,
                min_font_size = 10 ,).generate(comment_words_t1)

plt.figure(figsize = (8, 8), facecolor = 'green') 
plt.imshow(wordcloud_sw_t1) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show()

"""**Word Cloud for T2 after removing stopwords.**"""

wordcloud_sw_t2 = WordCloud(width = 800, height = 800, 
                background_color ='black', 
                stopwords = all_stopwords,
                min_font_size = 10 ,).generate(comment_words_t2)

plt.figure(figsize = (8, 8), facecolor = 'green') 
plt.imshow(wordcloud_sw_t2) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show()

wordlen_freq_t1 = {}
for item in tokens_t1:
  length = len(item)
  if(length == 18):
    print("18 length word : " + str(item))
  if(length == 23):
    print("23 length word : " + str(item))

  if length in wordlen_freq_t1:
    wordlen_freq_t1[length] = wordlen_freq_t1[length] + 1
  else:
    wordlen_freq_t1[length] = 1

print(wordlen_freq_t1)

lists_t1 = sorted(wordlen_freq_t1.items())
x1,y1=zip(*lists_t1)
plt.plot(x1,y1)
plt.xticks(range(0,24))
plt.rcParams["figure.figsize"] = (10,5)
plt.xlabel("Wordlength")
plt.ylabel("Frequency")
plt.title("Frequency v/s Word Length for T1")
plt.show()

wordlen_freq_t2 = {}
for item in tokens_t2:
  length = len(item)
  if(length == 24):
    print("24 length word : " + str(item))
  if(length == 27):
    print("27 length word : " + str(item))

  if length in wordlen_freq_t2:
    wordlen_freq_t2[length] = wordlen_freq_t2[length] + 1
  else:
    wordlen_freq_t2[length] = 1

print(wordlen_freq_t2)

lists_t2 = sorted(wordlen_freq_t2.items())
x2,y2=zip(*lists_t2)
plt.plot(x2,y2)
plt.rcParams["figure.figsize"] = (10,5)
plt.xticks(range(0,28))
plt.xlabel("Wordlength")
plt.ylabel("Frequency")
plt.title("Frequency v/s Word Length for T1")
plt.show()

plt.plot(x1, y1, label = "T1", lw=5, ls='--')
# plotting the line 2 points ,
plt.plot(x2, y2, label = "T2", lw=5)
plt.xlabel('Wordlength')
# Set the y axis label of the current axis.
plt.ylabel('Frequency')
plt.title('Wordlength and Frequency plot for T1 and T2')
plt.legend()
plt.rcParams["figure.figsize"] = (10,5)
plt.xticks(range(0,28))
plt.grid()
plt.show()

"""

> **PoS Tagging**

"""

nltk.download('universal_tagset')

"""**For T1**

"""

from nltk import pos_tag
nltk.download('averaged_perceptron_tagger')
nltk_data1 = pos_tag(tokens_t1)

type(nltk_data1)

for i in nltk_data1[0:10]:
  print(i)

"""**For T2**"""

nltk_data2 = pos_tag(tokens_t2)

for i in nltk_data2[0:10]:
  print(i)

from collections import Counter
counts = Counter(tag for word,tag in nltk_data1)
counts

list_noun1 = []
for item in nltk_data1:
  if(item[1]=="NN" or item[1]=="NNP" or item[1]=="NNPS" or item[1]=="NNS"):
    list_noun1.append(item)
##size(list_noun)

len(list_noun1)

print(list_noun1)

dict_noun1 = {}
from nltk.corpus import wordnet

for item in list_noun1:
  syn = wordnet.synsets(item[0])
  for i in syn:
    if i.lexname()[0]=='n':
      if i.lexname() in dict_noun1:
        dict_noun1[i.lexname()]+=1
      else:
        dict_noun1[i.lexname()]=1

print(dict_noun1)   
print(len(dict_noun1))

list_verb1 = []
for item in nltk_data1:
  if(item[1]=="VB" or item[1]=="VBD" or item[1]=="VBG" or item[1]=="VBN" or item[1]=="VBP" or item[1]=="VBZ"):
    list_verb1.append(item)

len(list_verb1)

print(list_verb1)

#for item in list_verb1:
#  print(syn = wordnet.synsets(item[0]))

dict_verb1 = {}

for item in list_verb1:
  syn = wordnet.synsets(item[0])
  for i in syn:
    if i.lexname()[0]=='v':
      if i.lexname() in dict_verb1:
        dict_verb1[i.lexname()]+=1
      else:
        dict_verb1[i.lexname()]=1

print(dict_verb1)   
print(len(dict_verb1))

"""For book2

"""

from collections import Counter
counts = Counter(tag for word,tag in nltk_data2)
counts

list_noun2 = []
for item in nltk_data2:
  if(item[1]=="NN" or item[1]=="NNP" or item[1]=="NNPS" or item[1]=="NNS"):
    list_noun2.append(item)

len(list_noun2)

len(list_noun2)
print(list_noun2)

dict_noun2 = {}
from nltk.corpus import wordnet

for item in list_noun2:
  syn = wordnet.synsets(item[0])
  for i in syn:
    if i.lexname()[0]=='n':
      if i.lexname() in dict_noun2:
        dict_noun2[i.lexname()]+=1
      else:
        dict_noun2[i.lexname()]=1

print(dict_noun2)   
print(len(dict_noun2))

list_verb2 = []
for item in nltk_data2:
  if(item[1]=="VB" or item[1]=="VBD" or item[1]=="VBG" or item[1]=="VBN" or item[1]=="VBP" or item[1]=="VBZ"):
    list_verb2.append(item)

len(list_verb2)

len(list_verb2)
print(list_verb2)

dict_verb2 = {}
from nltk.corpus import wordnet

for item in list_verb2:
  syn = wordnet.synsets(item[0])
  for i in syn:
    if i.lexname()[0]=='v':
      if i.lexname() in dict_verb2:
        dict_verb2[i.lexname()]+=1
      else:
        dict_verb2[i.lexname()]=1

print(dict_verb2)   
print(len(dict_verb2))

"""##Plotting histogram for Nouns and Verbs of Book 1"""

import matplotlib.pyplot as plt
import numpy as np

plt.bar(range(len(dict_noun1)), list(dict_noun1.values()), align = 'center')
plt.xticks(range(len(dict_noun1)), list(dict_noun1.keys()), rotation = 90)
plt.yticks(np.arange(0,12000,1000))

plt.bar(range(len(dict_verb1)), list(dict_verb1.values()), align = 'center')
plt.xticks(range(len(dict_verb1)), list(dict_verb1.keys()), rotation = 90)
plt.yticks(np.arange(0,45000,2000))

"""## Plotting Histogram for Nouns and Verbs for Book 2"""

plt.bar(range(len(dict_noun2)), list(dict_noun2.values()), align = 'center')
plt.xticks(range(len(dict_noun2)), list(dict_noun2.keys()), rotation = 90)
plt.yticks(np.arange(0,15000,1000))

plt.bar(range(len(dict_verb2)), list(dict_verb2.values()), align = 'center')
plt.xticks(range(len(dict_verb2)), list(dict_verb2.keys()), rotation = 90)
plt.yticks(np.arange(0,100000,5000))

"""**Recognising all entities like Persons, Location, Organisation in book.** """

import spacy
from spacy import displacy
import en_core_web_sm
nlp = en_core_web_sm.load()

doc = nlp(joined_book1)
print([(X.text, X.label_) for X in doc.ents])

sentences = [x for x in doc.sents]
print(sentences[30:50])

displacy.render(nlp(str(sentences[30:50])), jupyter=True, style='ent')

"""**Measuring accuracy**"""

parra_book1 = joined_book1[0:4000]
print(parra_book1)

doc1 = nlp(parra_book1)
print([(X.text, X.label_) for X in doc1.ents])

displacy.render(doc1, jupyter=True, style='ent')

"""Correctly lablelling the entities, which are incorrectly labelled in the selected parragraph

"""

manual_tagged_list = [('inch','QUANTITY'),('M.R.C.S.','PRODUCT'),('1884','DATE'),('Why so?','NULL'),('the Something Hunt','EVENT'),('the local hunt','EVENT'),('Watson','PERSON')]

correctly_labelled = len(doc1.ents)-len(manual_tagged_list)
Accuracy = correctly_labelled / len(doc1.ents)
print(Accuracy)

pip install stanford_openie

pip install stanza

import stanza
from stanza.server import CoreNLPClient
stanza.install_corenlp()
client = CoreNLPClient(timeout=150000000, be_quiet=True, annotators=['openie'], endpoint='http://localhost:9003')
document = client.annotate(joined_book1[0:50000], output_format='json')
triples = []
import en_core_web_sm
nlp = en_core_web_sm.load()
for sentence in document['sentences']:
    for triple in sentence['openie']:
      doc=nlp(triple['subject'])
      doc1=nlp(triple['object'])
      y=([X.label_ for X in doc.ents ])
      y1=([X.label_ for X in doc1.ents])
      #print(y,y1)
      if (y and y1 ):
        triples.append({
            'subject': (y,triple['subject']),
             'relation': triple['relation'],
              'object': (y1,triple['object'])
         })

for i in triples:
  print(i)
  print()

import stanza
from stanza.server import CoreNLPClient
stanza.install_corenlp()
client = CoreNLPClient(timeout=150000000, be_quiet=True, annotators=['openie'], endpoint='http://localhost:9003')
document = client.annotate(joined_book1[50000:100000], output_format='json')
#triples = []
import en_core_web_sm
nlp = en_core_web_sm.load()
for sentence in document['sentences']:
    for triple in sentence['openie']:
      doc=nlp(triple['subject'])
      doc1=nlp(triple['object'])
      y=([X.label_ for X in doc.ents ])
      y1=([X.label_ for X in doc1.ents])
      #print(y,y1)
      if (y and y1 ):
        triples.append({
            'subject': (y,triple['subject']),
             'relation': triple['relation'],
              'object': (y1,triple['object'])
         })

for i in triples:
  print(i)
  print()

document = client.annotate(joined_book1[100000:150000], output_format='json')
#triples = []
import en_core_web_sm
nlp = en_core_web_sm.load()
for sentence in document['sentences']:
    for triple in sentence['openie']:
      doc=nlp(triple['subject'])
      doc1=nlp(triple['object'])
      y=([X.label_ for X in doc.ents ])
      y1=([X.label_ for X in doc1.ents])
      #print(y,y1)
      if (y and y1 ):
        triples.append({
            'subject': (y,triple['subject']),
             'relation': triple['relation'],
              'object': (y1,triple['object'])
         })

for i in triples:
  print(i)
  print()

document = client.annotate(joined_book2[0:50000], output_format='json')
triples = []
import en_core_web_sm
nlp = en_core_web_sm.load()
for sentence in document['sentences']:
    for triple in sentence['openie']:
      doc=nlp(triple['subject'])
      doc1=nlp(triple['object'])
      y=([X.label_ for X in doc.ents ])
      y1=([X.label_ for X in doc1.ents])
      #print(y,y1)
      if (y and y1 ):
        triples.append({
            'subject': (y,triple['subject']),
             'relation': triple['relation'],
              'object': (y1,triple['object'])
         })

for i in triples:
  print(i)
  print()

document = client.annotate(joined_book2[50000:100000], output_format='json')
triples = []
import en_core_web_sm
nlp = en_core_web_sm.load()
for sentence in document['sentences']:
    for triple in sentence['openie']:
      doc=nlp(triple['subject'])
      doc1=nlp(triple['object'])
      y=([X.label_ for X in doc.ents ])
      y1=([X.label_ for X in doc1.ents])
      #print(y,y1)
      if (y and y1 ):
        triples.append({
            'subject': (y,triple['subject']),
             'relation': triple['relation'],
              'object': (y1,triple['object'])
         })

for i in triples:
  print(i)
  print()

document = client.annotate(joined_book2[100000:150000], output_format='json')
triples = []
import en_core_web_sm
nlp = en_core_web_sm.load()
for sentence in document['sentences']:
    for triple in sentence['openie']:
      doc=nlp(triple['subject'])
      doc1=nlp(triple['object'])
      y=([X.label_ for X in doc.ents ])
      y1=([X.label_ for X in doc1.ents])
      #print(y,y1)
      if (y and y1 ):
        triples.append({
            'subject': (y,triple['subject']),
             'relation': triple['relation'],
              'object': (y1,triple['object'])
         })

for i in triples:
  print(i)
  print()