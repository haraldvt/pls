from flask import Flask

app = Flask(__name__)


@app.route('/pls')
def pls():
    return 'PowerLineSwitching (pls)'

