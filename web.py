from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'


@app.errorhandler(404)
def not_found(error):
    return render_template('status404.html', title="404"), 404


if __name__ == "__main__":
    app.run()
