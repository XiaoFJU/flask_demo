from flask import Flask, request, render_template
from model.crawler import crawler

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'


@app.route('/page/<string:page>', methods=['GET'])
def show_page(page):
    if request.method == 'GET':
        return render_template('pages/{}.html'.format(page))


@app.route('/page/crawler', methods=['GET', 'POST'])
def page_crawler():
    if request.method == 'GET':
        return render_template('crawler.html')  
    if request.method == 'POST':
        file_name = request.form['file_name']
        url =  request.form['url']
        crawler(file_name, url)

        return 'OK', 200

if __name__ == "__main__":
    app.run()
