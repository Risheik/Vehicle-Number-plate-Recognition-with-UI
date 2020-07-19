from flask import Flask, request, jsonify, render_template
from subprocess import call
import pickle
app = Flask(__name__)


@app.route('/')
def CallPy(object):
        return render_template('main.py')

return render_template('main.py')