from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'


@app.route('/input',  methods=['GET'])
def input():
    return render_template('input.html')


if __name__ == "__main__":
    app.run()
