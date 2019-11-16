from flask import Flask, request, render_template, url_for, redirect, send_from_directory, session
from flask_login import LoginManager
import sqlite3
import random
import string
import os
from db.__init__ import *

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')

is_logged_in = False
app = Flask(__name__, template_folder=static_file_dir, static_folder=static_file_dir)
app.config['SECRET_KEY'] = 'AbReheSO2uksoMbZpagPHpuCdKY3R3DqiFIfLDy5K6I0XFOEOgMOfgwGB5pHeatI'


def connect_db():
    try:
        conn = sqlite3.connect('db/kommunity.db')
    except Error as e:
        print(e)

    cursor = conn.cursor()
    return cursor, conn

def generate_random(n=64):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(n))

@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('/about-us/index.html')

@app.route('/login')
def login():
    if not session.get('logged_in'):
        return render_template('/login/index.html')
    else:
        return redirect(url_for('recipes'))

# logout

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    post_username = str(request.form['username'])
    post_password = str(request.form['password'])
    
    cursor, conn = connect_db()
    result = cursor.execute('SELECT * from user WHERE username="' + post_username + '"').fetchone()
    
    print(result)
    if check_encrypted_password(post_password, result[3]):
        ingredients = result[4]
        session['logged_in'] = True
        conn.close()
        print(ingredients)
        return recipes(ingredients)
    else:
        conn.close()
        return redirect(url_for('login'))


@app.route('/recipes', defaults={'ingredients': None})
def recipes(ingredients):
    ingredients = ingredients.split(',')
    return render_template('/recipes/index.html', ingredients=ingredients)

if __name__ == "__main__":
    app.run(debug=True, port='5000')