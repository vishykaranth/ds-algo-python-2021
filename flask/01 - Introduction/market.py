from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)