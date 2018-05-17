from flask import Flask, request, render_template, render_template_string

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='%%%%',
        block_end_string='%%%%%>',
        variable_start_string='%%%',
        variable_end_string='%%%',
        comment_start_string='%%%%%',
        comment_end_string='%%%%%',
    ))

app = CustomFlask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return render_template('slides.html')


if __name__ == "__main__":
    app.run()
