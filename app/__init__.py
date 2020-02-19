from flask import Flask, render_template, jsonify
import requests, json
import app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sites')
def sites():
    data = json.load(open('sites.json'))
    return jsonify(data['sites'])
