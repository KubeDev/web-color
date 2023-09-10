from flask import Flask, render_template
from os import uname


app = Flask(__name__,
            template_folder='templates')

@app.route('/')
def index():

    return render_template('index.html', maquina=uname().nodename)

if __name__ == '__main__':
    app.run()