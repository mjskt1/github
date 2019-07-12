# from flask import Flask, render_template
#
# app = Flask(__name__)
#
#
# @app.route('/<string:username>')
# def index(username):
#     # return render_template('test.html')
#     return 'hello world! %s' % username
#
#
# if __name__ == '__main__':
#     app.run(host='192.168.196.130')

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<float:money>')
def index(money):
    # return render_template('test.html')
    return 'hello world! %s' % money


if __name__ == '__main__':
    app.run(host='192.168.196.130')
