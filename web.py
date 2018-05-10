from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()
