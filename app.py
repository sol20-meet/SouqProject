from flask import Flask, request, redirect, render_template
from flask import session as login_session
import pyrebase
import random
import os
from model import *

config = {
	"apiKey": "AIzaSyA7w5SIcYeKTrAwwrf8tTmHpVBaOiGY-As",
	"authDomain": "souq-project.firebaseapp.com",
	"databaseURL": "https://souq-project-default-rtdb.europe-west1.firebasedatabase.app",
	"projectId": "souq-project",
  	"storageBucket": "souq-project.appspot.com",
  	"messagingSenderId": "857179462787",
  	"appId": "1:857179462787:web:e2ab3d59ee6c00ac014fb6",
  	"measurementId": "G-JMQV717W13"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/about.html')
def About():
	return render_template('about.html')


@app.route('/upload.html' , methods=['GET','POST'])
def upload():
	if request.method == 'GET' :
		return render_template('upload.html')
	else:
		# print("creating Place object")
		# name_of_place = request.form['nameOfplace']
		# description = request.form['subject']
		# user = request.form['user']
		# link = request.form['Link']
		# #add_place is a function that creates a new object of a place based on the data that the user has entered in the webstie, and then it sends it to the database as a Place object.
		# if len(user) == 0:
		# 	user = "Anonymous User"
		# if len(link) == 0:
		# 	link = "https://wallpapercave.com/wp/wp4813075.jpg"

		# add_place(name_of_place , description , user , link)
		return redirect('list.html')


@app.route('/place.html/<int:p_id>')
def place(p_id):
	return render_template('place.html')



if __name__ == '__main__':
	app.run(debug=True)
