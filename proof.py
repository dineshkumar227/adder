from flask import Flask, request, render_template
from proof_parser import *
from test_code import *
from transpiler import *

app = Flask(__name__)

@app.route('/')
def proof_form():
	return render_template('proof-form.html')

@app.route('/', methods=['POST'])
def proof_form_post():
	text = request.form['text']
	a,b,c,d,e = parser(text)
	parsed_code = parse(a,b,c,d,e)
	code_file = open("/tmp/code_file.lean", "w")
	for i in parsed_code:
		code_file.write(i + "\n")
	code_file.close()
	messages = getErrors("/tmp/code_file.lean")
	print(messages)

	return render_template('output.html', messages=messages)

if __name__== "__main__":
	app.run()
