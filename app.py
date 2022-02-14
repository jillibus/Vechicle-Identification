from flask import Flask, render_template, redirect, url_for
#import pickle
#import pandas as pd

app = Flask(__name__)
#app = Flask(__name__, static_url_path="/cars_train", root_path="/cars_test")

@app.route('/')

def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()