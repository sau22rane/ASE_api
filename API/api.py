from flask import Flask, redirect, url_for, request

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

if __name__ == '__main__':
   app.run('0.0.0.0')