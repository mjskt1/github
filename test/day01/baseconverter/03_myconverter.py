from flask import Flask, render_template
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class MobileConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'


app.url_map.converters["number"] = MobileConverter


@app.route('/<number:num>')
def index(num):
    # return render_template('test.html')
    return 'hello world! %s' % num


if __name__ == '__main__':
    app.run(host='192.168.196.130')
