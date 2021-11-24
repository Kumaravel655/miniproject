from flask import Flask, render_template

app = Flask(__name__)

@app.route('/org.html')

def org():
    return render_template('org.html')



@app.route('/topic.html')
def topic():
    return render_template('topic.html')
@app.route('/sub.html')
def sub():
    return render_template('sub.html')

@app.route('/sample.html')
def sample():
    return render_template('sample.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home.html')
def home1():
    return render_template('home.html')

