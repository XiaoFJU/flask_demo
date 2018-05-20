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


@app.route('/bmi',  methods=['GET', 'POST'])
def bmi():
    if request.method == 'GET':
        return render_template('bmi.html')
    elif request.method == 'POST':
        name = '乂煞氣a' + request.form['name'] + '乂'
        weight = float(request.form['weight'])
        height = float(request.form['height'])

        # calculate bmi
        bmi = weight / (height**2)

        if bmi < 18.5:
            result = '過輕'
        elif 18.5 <= bmi <= 24:
            result = '正常'
        elif 24 < bmi:
            result = '過重'

        return render_template('bmi_result.html',
                               name=name,
                               bmi=bmi,
                               result=result)


if __name__ == "__main__":
    app.run()
