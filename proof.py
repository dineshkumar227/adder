from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def proof_form():
    return render_template('proof-form.html')

@app.route('/', methods=['POST'])
def proof_form_post():
    text = request.form['text']
    return "succ the zucc" 

if __name__== "__main__":
    app.run()
