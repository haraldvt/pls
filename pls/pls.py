from flask import Flask

app = Flask(__name__)


@app.route('/pls')
def hello():
    return 'PowerLineSwitching (pls) in aanbouw'

