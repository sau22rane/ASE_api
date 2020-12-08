from flask import Flask, redirect, url_for, request
from utils import load_coords, get_coords, get_score, rescale, match, poseScore, angleScore
import json
import numpy as np
import math

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def init():
   if request.method == 'POST':
      course = request.form['course']
      asana = request.form['asana']
      return 'Welcome to {} course. Today we\'ll learn {} asana.'.format(course, asana)
   else:
      course = request.args.get('course')
      asana = request.args.get('asana')
      return 'Welcome to {} course. Today we\'ll learn {} asana.'.format(course, asana)

@app.route('/getScore/', methods = ['POST', 'GET'])
def score():
   if request.method == 'POST':
      course = request.form['course']
      asana = request.form['asana']
      cords_data = request.form['cords']
   else:
      course = request.args.get('course')
      asana = request.args.get('asana')
      cords_data = request.args.get('cords')
   cords_data = "{"+ cords_data +"}"
   a = load_coords(course,  asana)
   print(a)
   b = get_coords(json.loads(cords_data))
   ret, b = rescale(b)
   print(b)
   return str(get_score(a,b))
   
if __name__ == '__main__':
   app.run('0.0.0.0')


