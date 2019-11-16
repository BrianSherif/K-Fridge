from flask import Flask, request, render_template, url_for, send_from_directory
import os

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')

app = Flask(__name__, template_folder=static_file_dir, static_folder=static_file_dir)


@app.route('/home')
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('/about-us/index.html')

if __name__ == "__main__":
    app.run(debug=True, port='5000')