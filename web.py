from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'


@app.route('/input',  methods=['GET'])
def input():
    return '''
        <form action="/input" method="post">
            名字是: <input type="text" name="name"><br>
            ID 是: <input type="text" name="id"><br>
            <input type="submit" value="Submit">
        </form>
    '''


if __name__ == "__main__":
    app.run()
