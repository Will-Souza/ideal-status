from flask import Flask, render_template, jsonify
import requests, json
import app

app = Flask(__name__)

data = json.load(open('sites.json'))

@app.route('/')
def index():
    return render_template('index.html', data=len(data['sites']))

@app.route('/sites')
def sites():
    return jsonify(data['sites'])
