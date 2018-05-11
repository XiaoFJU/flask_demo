from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'


@app.route('/input',  methods=['GET', 'POST'])
def input():
    if request.method == 'GET':
        return render_template('input.html')
    elif request.method == 'POST':
        name = '乂煞氣a' + request.form['name'] + '乂'
        id = request.form['id']
        
        return render_template('self_introduction.html',
                               name=name,
                               id=id)


if __name__ == "__main__":
    app.run()
