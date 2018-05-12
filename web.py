from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'


@app.route('/page/<string:page>', methods=['GET'])
def show_page(page):
    if request.method == 'GET':
        return render_template('pages/{}.html'.format(page))


if __name__ == "__main__":
    app.run()
