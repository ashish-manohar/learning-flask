from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hi! I'm Ashish. I'm trying to learn python."

@app.route('/me')
def my_info():
    return "My Name is Ashish."

if __name__ == '__main__':
    app.run()