from flask import Flask, render_template
import time

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
  plscontext =  {
    'date' :  time.strftime("%c"),
    'user' : {'username': 'Harald'},
    'version': '0.0.3'
   }
   
  return render_template('index.html', plscontext = plscontext)

@app.route('/pls')
def pls():
    return 'PowerLineSwitching (pls)'

