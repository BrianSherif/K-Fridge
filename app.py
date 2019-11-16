from flask import Flask, request, render_template, url_for, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_socketio import SocketIO, send
import os

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')

app = Flask(__name__, template_folder=static_file_dir, static_folder=static_file_dir)


engine = create_engine('sqlite:///db/kommunity.db', echo=True)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/kommunity.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'AbReheSO2uksoMbZpagPHpuCdKY3R3DqiFIfLDy5K6I0XFOEOgMOfgwGB5pHeatI'
db = SQLAlchemy(app)
socketio = SocketIO(app)

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
    if session.get('userid'):
        return redirect(url_for('recipes'))
    else:
        return render_template('/login/index.html')

# logout

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    post_username = str(request.form['username'])
    post_password = str(request.form['password'])

    random_token = generate_random()
    # print(random_token)
    session[random_token] = {
        'username': post_username,
        'password': post_password
    }
    
    return redirect(url_for('login_auth', token=random_token))

@app.route('/login-auth/<token>')
def login_auth(token):
    if not session[token]:
        return redirect(url_for('recipes'))
    post_username = session[token]['username']
    post_password = session[token]['password']
    session.pop(token, None)

    Session = sessionmaker(bind=engine)
    s = Session()

    result = s.query(user).filter(user.username.in_([post_username]), user.password.in_([post_password])).first()
    print(result)
    if result:
        query = s.query(user).filter(user.username.in_([post_username])).first()
        ingredients = query.items
        session['logged_in'] = True
        session['userid'] = query.userid
        return redirect(url_for('recipes', user=query))
    else:
        return redirect(url_for('login'))


@app.route('/recipes', defaults={'user': None})
def recipes(user):
    return render_template('/recipes/index.html')

if __name__ == "__main__":
    app.run(debug=True, port='5000')