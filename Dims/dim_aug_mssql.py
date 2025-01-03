﻿import pyodbc 
import os, io

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-D39A2O2\SQLEXPRESS;'
                      'Database=model;'
                      'Trusted_Connection=yes;')
					  
datafile = 'aug_dim_tab.txt'
DBNAME = 'model'

def file_to_list(file_name):
    fr = io.open(file_name, encoding = 'utf-8')
    l = [line.strip().split('\t') for line in fr]
    l.sort(key = lambda line: line[1].lower())
    l.sort(key = lambda line: line[5].lower())
    fr.close()
    return l

def get_data(l):
    lexems, lemmas = [], []
    j = 0
    for i in range(len(l)):
        lem = l[i]
        if lem[5] not in lexems:
            j += 1
            lexems.append(lem[5])
            lemmas.append((lem[0], lem[1], lem[2], lem[3], lem[4], j))
            print(lem[5])
        else:
            lex_index = lexems.index(lem[5]) + 1
            lemmas.append((lem[0], lem[1], lem[2], lem[3], lem[4], lex_index))
    return lexems, lemmas

def fill_db(lexemes):
    print('filling database...1')
    with pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-D39A2O2\SQLEXPRESS;'
                      'Database=model;'
                      'Trusted_Connection=yes;') as conn:
        print('filling database...2')
        cursor = conn.cursor()
        print(lexemes)
        print('filling database...3')
        cursor.executemany("""insert into model.dbo.Lexeme(lex) values (?)""", lexemes) 
        cursor.commit()
        print('filling database...4')
        cursor.executemany("""insert into  model.dbo.Lemma(lemtype, lem, suffix, tag, descr, lexid) values (?, ?, ?, ?, ?, ?)""", lemmas)    
        print('filling database...5')
        cursor.commit()

def query_db(dbname):
    with pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-D39A2O2\SQLEXPRESS;'
                      'Database=model;'
                      'Trusted_Connection=yes;') as conn:
        print('querying database...')

        print('--- Lexeme:')
        cursor = conn.cursor()
        cursor.execute('select * from dbo.Lexeme LIMIT 5;')
        for row in cursor.fetchall():
            lexid, lex = row
            print(lexid, lex)
        
        print('--- Lemma:')
        cursor = conn.cursor()
        cursor.execute('select * from dbo.Lemma LIMIT 5;')
        for row in cursor.fetchall():
            lemid, lemtype, lem, suffix, tag, descr, lexid = row
            print(lemid, lemtype, lem, suffix, tag, descr, lexid) 

        for row in cursor.fetchall():
            lem, lex = row
            print(lex, lem) 
        cursor.commit()

if __name__ == '__main__':
    
    l = file_to_list(datafile)
    lexemes, lemmas = get_data(l)
    
    # --- prepare DB
    Output = tuple([name] for name in lexemes) 
    Output2 = tuple([name] for name in lemmas) 
    fill_db(Output)
    fill_db(Output2)

    # --- query DB
    #query_db(DBNAME)