#!/usr/bin/env python3
from flask import Flask, render_template, jsonify,flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from app import *
import os
import random
import string

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), "static", "videos")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

current_file_num = 16

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/home")
def home_html():
    return render_template("home_page.html")

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/squat")
def squat():
    return render_template("squat.html")


@app.route("/bench")
def bench():
    return render_template("bench.html")


@app.route("/deadlift")
def deadlift():
    return render_template("deadlift.html")


@app.route("/squatupload")
def squatupload():
    return render_template("squat_upload.html")


@app.route("/benchupload")
def benchupload():
    return render_template("bench_upload.html")


@app.route("/deadliftupload")
def deadliftupload():
    return render_template("deadlift_upload.html")


@app.route('/video/<videostr>')
def video(videostr):
    print(videostr)
    vid_path = 'videos/' + videostr
    return render_template("video.html", value=vid_path)


@app.route('/deadlift_info', methods=['GET'])
def get_deadlift_info():
    return printDeadliftJson()


@app.route('/squat_info', methods=['GET'])
def get_squat_info():
    return printSquatJson()


@app.route('/bench_info', methods=['GET'])
def get_bench_info():
    return printBenchJson()


@app.route('/logincred', methods=['GET'])
def cred():
    user = request.args.get('login')
    password = request.args.get('password')
    return validateUser(user, password)


@app.route('/create_account', methods=['GET'])
def create_account():
    user = request.args.get('login')
    password = request.args.get('password')
    if validateUsername(user):
        return "false"
    add_to_accounts(user, password)
    return "true"
    

@app.route('/delete_entry', methods=['GET'])
def delete():
    delVid = request.args.get('delete')
    delete_vid(delVid)
    return ""


@app.route('/squat_upload_endpoint', methods = ['POST'])  
def squat_upload_endpoint():  
    try:
        if request.method == 'POST':  
            global current_file_num 
            f = request.files['file']  
            weight = request.values['weight']
            rep = request.values['reps']
            f = request.files['file']  
            filename = str(current_file_num) + ".mov"
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)))
            current_file_num += 1     
            addSquat(weight, rep, filename)
            return render_template("redirect_squat.html")  
    except:
        return render_template("redirect_bench.html") 


@app.route('/bench_upload_endpoint', methods = ['POST'])  
def bench_upload_enpoint():  
    try:
        if request.method == 'POST': 
            global current_file_num 
            f = request.files['file']  
            weight = request.values['weight']
            rep = request.values['reps']
            f = request.files['file']  
            filename = str(current_file_num) + ".mov"
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)))
            current_file_num += 1           
            addBench(weight, rep, filename)
            return render_template("redirect_bench.html") 
    except Exception as e: 
        print(e)
        print('bad')
        return render_template("redirect_bench.html") 


@app.route('/deadlift_upload_endpoint', methods = ['POST'])  
def deadlift_upload_endpoint():  
    try:
        if request.method == 'POST':  
            global current_file_num 
            f = request.files['file']  
            weight = request.values['weight']
            rep = request.values['reps']
            f = request.files['file']  
            filename = str(current_file_num) + ".mov"
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)))
            current_file_num += 1     
            addDeadlift(weight, rep, filename)
            return render_template("redirect_deadlift.html")  
    except:
        return render_template("redirect_bench.html") 

if __name__ == "__main__":
    app.run(debug=True)
