from flask import Flask, request, render_template
from model.crawler import crawler
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)

jinja_options = app.jinja_options.copy()
jinja_options.update(dict(
    block_start_string='{{%',
    block_end_string='%}}',
    variable_start_string='{{<',
    variable_end_string='>}}',
    comment_start_string='{{#',
    comment_end_string='#}}',
))
app.jinja_options = jinja_options

@app.route('/slide', methods=['GET'])
def slide():
    return render_template('slides.html')


# first
@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'


# url parameter
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


# input
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


# bmi
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


# crawler
@app.route('/page/crawler', methods=['GET', 'POST'])
def page_crawler():
    if request.method == 'GET':
        return render_template('crawler.html')  
    if request.method == 'POST':
        file_name = request.form['file_name']
        url =  request.form['url']
        crawler(file_name, url)

        return 'OK', 200

@app.route('/page/<string:page>', methods=['GET'])
def show_page(page):
    if request.method == 'GET':
        return render_template('pages/{}.html'.format(page))


# SQLi
@app.route('/sqli')
def sqli():
    return render_template('sqli.html', title='SQLi')


# error handle
@app.errorhandler(404)
def not_found(error):
    return render_template('status404.html', title="404"), 404

@app.errorhandler(TemplateNotFound)
def handle_template_not_found(error):
    return '我悶迷U J格葉面'


if __name__ == "__main__":
    app.run()
