import os
from flask import Flask, render_template, request, flash, redirect
import pyodbc
import codecs
import subprocess


app = Flask(__name__)

def file_to_list(file_name):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    file_url = os.path.join(SITE_ROOT, 'static', file_name)    
    with open(file_url, encoding='utf-8') as fr:
        l = [line.strip() for line in fr]
        fr.close()
    return l

def search_by_lem(lemma):
    with pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-D39A2O2\SQLEXPRESS;'
                      'Database=model;'
                      'Trusted_Connection=yes;') as conn:
        #cursor = conn.cursor()
        #lemma = request.form.get('lem')
        conn.autocommit = True
        form0 = conn.execute(
            """SELECT model.dbo.Lemma.lemtype, model.dbo.Lexeme.lex, model.dbo.Lemma.suffix, model.dbo.Lemma.tag, model.dbo.Lemma.descr
                FROM model.dbo.Lemma
                JOIN model.dbo.Lexeme ON model.dbo.Lexeme.lexid = Lemma.lexid
                WHERE model.dbo.Lemma.lem= ?;""", lemma)#.fetchall
        #conn.commit()
        form = (form0.fetchall())
        #print(form.fetchall())
        #conn.close()
        #for row in form:
            #print(row)
    #print(form)
    return form


def search_by_lex(lexeme, lemtype, suffix, suf_meaning):
    with pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-D39A2O2\SQLEXPRESS;'
                      'Database=model;'
                      'Trusted_Connection=yes;') as conn:
        conn.autocommit = True
        sql = """SELECT dbo.Lemma.lem, dbo.Lexeme.lex, dbo.Lemma.suffix, dbo.Lemma.tag, dbo.Lemma.descr
                    FROM dbo.Lemma
                    JOIN dbo.Lexeme ON dbo.Lexeme.lexid = dbo.Lemma.lexid
                    WHERE """
        #conn.autocommit = True

        if lexeme != '':
            sql += "Lexeme.lex = '" + lexeme + "' AND "
   
        if suffix != []:
            suf_sql = []
            for i in range(len(suffix)):
                suf_sql.append("Lemma.suffix = '" + suffix[i] + "'")
            sql += "(" + " OR ".join(suf_sql) + ") AND "

        #if suf_meaning != []:
         #   suf_meaning_sql = []
          #  for i in range(len(suf_meaning)):
           #     suf_meaning_sql.append("Lemma.tag like '%" + suf_meaning[i] + "%'")
            #sql += "(" + " OR ".join(suf_meaning_sql) + ") AND "
         
        if lemtype != '':
            sql += "Lemma.lemtype = '" + lemtype + "'"
            #conn.execute(sql)#.fetchall
            #dim = conn.commit()
            #aug = ()
            dim0 = conn.execute(sql)
            dim = dim0.fetchall()
            aug = ()
        elif lemtype == 'a':
            conn.execute(sql + "Lemma.lemtype = 'a';")#.fetchall
            aug = conn.commit()
            dim = ()
        else:
            conn.execute(sql + "Lemma.lemtype = 'd';")#.fetchall
            dim = conn.commit()
            conn.execute(sql + "Lemma.lemtype = 'a';")#.fetchall
            aug = conn.commit()
        conn.commit()
        print(sql)
        return dim, aug

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/result')
#def getfact():
#    return render_template('extract.html')

@app.route('/search',methods = ['GET'])
def search():
    suffixes_d = file_to_list('suffixes_d.txt')
    suf_meanings_d = file_to_list('suf_meanings_d.txt')
    suffixes_a = file_to_list('suffixes_a.txt')
    suf_meanings_a = file_to_list('suf_meanings_a.txt')
    return render_template('search.html', suffixes_d = suffixes_d, suf_meanings_d = suf_meanings_d,
                           suffixes_a = suffixes_a, suf_meanings_a = suf_meanings_a)

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/exercises')
def exercises():
    #txt0 = request.form['txt']
    #print("The text", txt0)
    return render_template('exercises.html')
    #return "Thanks"
@app.route('/extract', methods=["post"])
def extract():
    txt0 = request.form['txt']
    with codecs.open('C:/Users/ILLA_0/Desktop/db_dims/dims/dims/tomita/input/input.txt', 'w', 'utf-8') as f:
            f.write(str(txt0))
    cmd = ['C:/Users/ILLA_0/Desktop/db_dims/dims/dims/tomita/tomita.bat']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    print(p)
    for line in p.stdout:
        print(line)
    p.wait()
    print(p.returncode)
    #process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    #process.wait()
    #p=subprocess.run(['G:/dims/tomita/tomita.bat'], capture_output=True)
    #print(p.stdout.decode())
    #print(p.stderr.decode()
    print("The text", txt0)
    return render_template('pretty.html')
    #return "Thanks"

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        lemma = ''
        print(lemma)
        if 'lem' in result:
            lemma = result['lem']
            form = search_by_lem(lemma)
            #print(form.fetchall())
            if form == []:
                lemma = ' '
            return render_template("result.html", lemma = lemma, form = form)
        else:
            lexeme = result['lex']
            lemtype = 'all'
            suffix = request.form.getlist('suffix')
            suf_meaning = request.form.getlist('suf_meaning')            
            if 'lemtype' in result:
                lemtype = result['lemtype']
            dim, aug = search_by_lex(lexeme, lemtype, suffix, suf_meaning)
            return render_template("result.html", lexeme = lexeme, lemma = lemma, dim = dim, aug = aug)  
 
if __name__ == "__main__":
    app.run(debug = True)

