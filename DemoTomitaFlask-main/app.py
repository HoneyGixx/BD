import codecs
import subprocess
import os
from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercises')
def exercises():
    #txt0 = request.form['txt']
    #print("The text", txt0)
    return render_template('exercises.html')
    #return "Thanks"	

#txt0 = 'котик домик комп. Белый дом. Синий утес в томске'
#D:\tomita\demo
@app.route('/extract', methods=["post"])
def extract():
	txt0 = request.form['txt']
	##
	#run tomita for single file 
	with codecs.open('./test.txt', 'w', 'utf-8') as f:
		f.write(str(txt0))
		
	cmd = ["./tomitaparser.exe config.proto"]
	command = ['./tomitaparser.exe', 'config.proto']
	# Run the command and capture the output
	output = subprocess.check_output(command)
	##
	return render_template('pretty.html')
#	cmd = ["D:/tomita/demo/tomitaparser.exe config.proto"]
#p = subprocess.Popen(cmd)

#print(p)

#	command = ['D:/tomita/demo/tomitaparser.exe', 'config.proto']
# Run the command and capture the output
#	output = subprocess.check_output(command)
# Print the output
	#print(output)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
