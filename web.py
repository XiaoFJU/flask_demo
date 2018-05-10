from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'


@app.route('/user/<name>')
def hello_for(name):
    return 'Hello, ' + name


@app.route('/id/<int:user_id>')  # 可以指定型態!!
def hello_for_id(user_id):
    # 如果他是字串的話，會出現10次 id
    return 'Your ID*10 = ' + str(user_id * 10)


@app.route('/user/<string:name>/hw<int:hw>')  # 可以有多個參數
def user_homework(name, hw):
    return '<h1>Hello, {}. this is homeWork{}</h1>'.format(name, hw)


if __name__ == "__main__":
    app.run()
