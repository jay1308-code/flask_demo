from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    name = 'jay pandya'
    return f'Hi, my name is {name}'

if __name__ == '__main__':
    app.run(debug=True)
