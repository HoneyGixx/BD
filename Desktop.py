#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request, flash, redirect
import os 
import pyodbc
import codecs
import subprocess


# In[78]:


with pyodbc.connect('Driver={SQL Server};'
                      'Server=WIN-01PF0KTEPI9;'
                      'Database=ngram;'
                      'Trusted_Connection=yes;') as conn:
        print('filling database...2')
        cursor = conn.cursor()
        print('filling database...4')
        cursor.execute("""insert into  dbo.Text(Text, Phrase) values ('Я видел сегодня большой Американский белый дом', 'белый дом')""")    
        print('filling database...5')
        cursor.commit()


# In[4]:


def fill_db(phrase):
    print('filling database...1')
    with pyodbc.connect('Driver={SQL Server};'
                      'Server=WIN-01PF0KTEPI9;'
                      'Database=ngram;'
                      'Trusted_Connection=yes;') as conn:
        print('filling database...2')
        cursor = conn.cursor()
        print('filling database...4')
        cursor.executemany("""insert into  dbo.Text(Text, Phrase) values ( ?, ?)""", phrase)    
        print('filling database...5')
        cursor.commit()


# In[5]:


tt = ('Я ем вкусную шоколадку', 'вкусную шоколадку')
fill_db([tt])


# In[6]:


print(tt)


# In[7]:


with pyodbc.connect('Driver={SQL Server};'
                      'Server=WIN-01PF0KTEPI9;'
                      'Database=ngram;'
                      'Trusted_Connection=yes;') as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM dbo.Text where Phrase = 'вкусную шоколадку'""")   
        #cursor.commit()
        records = cursor.fetchall()

print(records)


# In[7]:


import nltk 
import requests
import html5lib
import lxml
from bs4 import BeautifulSoup
import subprocess
import pandas as pd
from bs4 import BeautifulSoup


# In[3]:


# Read the HTML file into a Pandas dataframe
with open('test.html', encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')
tables = pd.read_html(str(soup))


# In[4]:


text = "Сегодня теплый день."


# In[14]:


with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(str(text))


# In[15]:


def extract():
	#txt0 = text
	##
	#run tomita for single file 
	#with codecs.open('tomita app/test.txt', 'w', 'utf-8') as f:
	#	f.write(str(txt0))
		
	#cmd = ["./tomita app/tomitaparser.exe ./tomita app/config.proto"]
	command = ['./tomitaparser.exe', './config.proto']
	# Run the command and capture the output
	output = subprocess.check_output(command)
	##
	#return render_template('pretty.html')


# In[16]:


extract()


# In[5]:


def tomparce(x):
    with open(x, encoding="utf-8") as file:
        soup = BeautifulSoup(file, 'html.parser')
    tables = pd.read_html(str(soup))
    return(tables)


# In[8]:


rslt = tomparce('./templates/pretty.html')[0]


# In[9]:


rslt


# In[23]:


nltk.download('punkt')


# In[11]:


rslt['toks'] = rslt.apply(lambda row: nltk.word_tokenize(row['Text']), axis=1)


# In[3]:


text = "Сегодня теплый день и солнце играет яркими красками на белоснежном снегу, покрывающим огромные крыши заброшенных домов."
text


# In[5]:


import nltk
nltk.download('wordnet')


# In[34]:


def create_connection():
    with pyodbc.connect('Driver={SQL Server};'
                      'Server=WIN-01PF0KTEPI9;'
                      'Database=ngram;'
                      'Trusted_Connection=yes;') as conn:
        try:
            print('connecting to database...')
            cursor = conn.cursor()
            print("Connection to DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return cursor


# In[35]:


connection = create_connection()


# In[8]:


#Execute SQL write to DB
def execute_write_query(connection, text):
    for d in text:
        print(d)
    cursor.execute(" insert into dbo.Text(dbo.Text, Phrase) values (?, ?) ", d)
    cursor.commit()


# In[45]:


def execute_write_pos(connection, text, phrase):
    #cursor = connection.cursor()
    #TId = execute_read_query(connection, """SELECT TOP 1 IDText FROM ngram.dbo.Text ORDER BY IDText DESC""")
    #key = TId[0][0] + 1
    #ins = [key, text]
    cursor.executemany(""" insert into dbo.Text( Text) values ( ?);""", [text])
    cursor.commit()
    cursor.executemany(""" insert into dbo.Text( Phrase) values ( ?);""", [phrase[0][0]])
    cursor.commit()


# In[7]:


#Execute SQL read DB
def execute_read_query(connection, query):
    #cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# In[8]:


text


# In[9]:


def extract():
	#txt0 = text
	##
	#run tomita for single file 
	#with codecs.open('tomita app/test.txt', 'w', 'utf-8') as f:
	#	f.write(str(txt0))
		
	#cmd = ["./tomita app/tomitaparser.exe ./tomita app/config.proto"]
	command = ['./tomitaparser.exe', './config.proto']
	# Run the command and capture the output
	output = subprocess.check_output(command)
	##
	#return render_template('pretty.html')


# In[10]:


with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(str(text))


# In[11]:


extract()


# In[12]:


def tomparce(x):
    with open(x, encoding="utf-8") as file:
        soup = BeautifulSoup(file, 'html.parser')
    tables = pd.read_html(str(soup))
    return(tables)


# In[13]:


def tknz(wrd):
    word_list = nltk.word_tokenize(wrd)
    return(word_list)


# In[14]:


rslt = tomparce('./templates/pretty.html')[0]


# In[15]:


#Tokens
rslt['toks'] = rslt.apply(lambda row: nltk.word_tokenize(row['Text']), axis=1)


# In[16]:


rslt['txt']=text
rslt


# In[17]:


#Ecec to DB
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WIN-01PF0KTEPI9;'
                      'Database=ngram;'
                      'Trusted_Connection=yes;')
cursor = cnxn.cursor()

# Insert Dataframe into SQL Server:
for index, row in rslt.iterrows():
     cursor.execute("insert into dbo.Text(dbo.Text, Phrase) values (?, ?)", row.txt, row.Text)
cnxn.commit()
cursor.close()


# In[24]:


#def getTextID(x):
def getIDText(ph):
    phr = ph
    with pyodbc.connect('Driver={SQL Server};'
                      'Server=WIN-01PF0KTEPI9;'
                      'Database=ngram;'
                      'Trusted_Connection=yes;') as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT IDText FROM dbo.Text where Phrase = ?;""", phr)   
        #cursor.commit()
        records = cursor.fetchall()
        cursor.close
    return(records[0][0])


# In[25]:


print(getIDText("теплый день"))


# In[26]:


rslt['Text'][0]


# In[27]:


rslt['toks'][0][0]


# In[28]:


tf = []


for i in range(len(rslt['toks'])):
    for j in range(len(rslt['toks'][i])):  
        tf.append((rslt['toks'][i][j], getIDText(rslt['Text'][i])))

print(tf)


# In[29]:


#Structure
cort = ()
wrd = []
PhData= ()
lst = []
for i in range(len(rslt['toks'])):
    #print(rslt['toks'][i][0])
    wrd = rslt['toks'][i][0]
    idT = getIDText(rslt['Text'][i])
    PhData = wrd, idT
    if len(PhData)==0:
        lst.append(PhData)
        wrd = ''
        wrd = ''
        wrd = rslt['toks'][i][1]
    #PhData =  (PhData, (wrd, idT))
        #PhData = PhData, (wrd,idT)
        i=i+1
    else:#print(PhData)
        wrd = rslt['toks'][i][0]
        idT = getIDText(rslt['Text'][i])
        PhData = wrd, idT
        lst.append(PhData)
        wrd = ''
        wrd = rslt['toks'][i][1]
    #PhData =  (PhData, (wrd, idT))
        #PhData = PhData, (wrd,idT)
        print(lst)
        PhData = ''
        wrd = ''
        idT = ''
        i=i+1


# In[35]:


def write_rightphrase(text):
    print('filling database...1')
    with pyodbc.connect('Driver={SQL Server};'
                      'Server=WIN-01PF0KTEPI9;'
                      'Database=ngram;'
                      'Trusted_Connection=yes;') as conn:
        print('filling database...2')
        cursor = conn.cursor()
        print('filling database...4')
        cursor.executemany("""insert into  dbo.Ngram(dbo.Word, IDText) values ( ?, ?)""", text)    
        print('filling database...5')
        cursor.commit()


# In[36]:


write_rightphrase(lst)


# In[21]:


from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    Doc
)


# In[22]:


def extrpos(sent):
    morph_vocab = MorphVocab()
    segmenter = Segmenter()
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    syntax_parser = NewsSyntaxParser(emb)
    doc = Doc(sent)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    return(doc)


# In[ ]:


doc()


# In[41]:


#checkpos = extrpos(rslt['Text'][1][0])
rslt['Text'][0]


# In[42]:


rslt['txt'][0]


# In[43]:


fullstring = rslt['txt'][0]
substring = rslt['Text'][0]
if substring in fullstring:
    print("Подстрока найдена!")
else:
    print("Подстрока не найдена!")
    
try:
    fullstring.index(substring)
except ValueError:
    print("Подстрока не найдена!")
else:
    print("Подстрока найдена!")
    
if fullstring.find(substring) != -1:
    print("Подстрока найдена!")
else:
    print("Подстрока не найдена!")

from re import search
if search(substring, fullstring):
    print("Подстрока найдена!")
else:
    print("Подстрока не найдена!")


# In[44]:


checkpos = extrpos(rslt['Text'][1])


# In[45]:


for token in checkpos.tokens:
    print(token.pos, token.text)


# In[46]:


def getIDWord(ph):
    phr = ph
    with pyodbc.connect('Driver={SQL Server};'
                      'Server=WIN-01PF0KTEPI9;'
                      'Database=ngram;'
                      'Trusted_Connection=yes;') as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT IDWord FROM dbo.Ngram where Word = ?;""", phr)   
        #cursor.commit()
        records = cursor.fetchall()
        cursor.close
    return(records[0][0])


# In[53]:


getIDWord('яркий')


# In[52]:


getIDWord(rslt['toks'][0][0])
for token in doc.tokens:
    print(token.pos, token.text)


# In[16]:


pip install pymystem3


# In[17]:


from pymystem3 import Mystem
m = Mystem()
def lemmatize_sentence(text):    
    lemmas = m.lemmatize(text)
    return "".join(lemmas).strip()


# In[18]:


def extrpos(sent):    
    morph_vocab = MorphVocab()
    segmenter = Segmenter()    
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)    
    syntax_parser = NewsSyntaxParser(emb)
    doc = Doc(sent)    
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)    
    return(doc)


# In[38]:


def getIDWord(ph):
    phr = ph
    with pyodbc.connect('Driver={SQL Server};'
                      'Server=WIN-01PF0KTEPI9;'
                      'Database=ngram;'
                      'Trusted_Connection=yes;') as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT IDWord FROM dbo.Ngram where Word = ?;""", phr)   
        #cursor.commit()
        records = cursor.fetchall()
        cursor.close
    return(records[0][0])


# In[30]:


lst = []
tmp = ()
posW = ()
nm=()
nmW=()
doc=""
#lemmatize_sentence

for i in range(len(rslt['toks'])):    
    #tmp = tmp + (lemmatize_sentence(rslt['toks'][i][0]),) 
    tmp = tmp + (lemmatize_sentence(rslt['toks'][i][0]),)    
    doc = extrpos(rslt['toks'][i][0])
    tmp = tmp + (doc.tokens[0].pos,)    
    nm =  str(getIDText(rslt['Text'][i]))
    nmW = str(getIDWord(rslt['toks'][i][0]))    
    tmp = tmp + (nmW,)
    tmp = tmp + (nm,)    
    lst.append(tmp)
    tmp = ()    
    #print(tmp)
    #tmp =  tmp + (lemmatize_sentence(rslt['toks'][i][1]),)    
    tmp = tmp + (lemmatize_sentence(rslt['toks'][i][1]),)
    doc = extrpos(rslt['toks'][i][1])    
    tmp = tmp + (doc.tokens[0].pos,)
    nm =  str(getIDText(rslt['Text'][i]))    
    nmW =  str(getIDWord(rslt['toks'][i][0]))
    tmp =  tmp + (nmW,)    
    tmp =  tmp + (nm,)
    lst.append(tmp)    
    tmp = ()
print(lst)


# In[58]:


def execute_pos_toks(connection,tt):  
    with pyodbc.connect('Driver={SQL Server};'
                      'Server=WIN-01PF0KTEPI9;'
                      'Database=ngram;'
                      'Trusted_Connection=yes;') as conn:
        for d in tt:
            print(d)
    cursor = conn.cursor()
    cursor.executemany(" insert into dbo.Lem(Lem, PoS, IDWord, IDText) values (?, ?, ?, ?) ", d)   
    #cursor.commit()
    cursor.close
    


# In[59]:


execute_pos_toks(connection, [lst])


# In[ ]:


#

