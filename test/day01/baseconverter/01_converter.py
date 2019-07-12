# from flask import Flask, render_template
# 
# app = Flask(__name__)
# 
# 
# @app.route('/<user_id>')
# def index(user_id):
#     return 'hello world! %s' % user_id
# 
# 
# if __name__ == '__main__':
#     app.run(host='192.168.196.130')


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<int:user_id>')
def index(user_id):
    # return render_template('test.html')
    return 'hello world! %s' % user_id


if __name__ == '__main__':
    app.run(host='192.168.196.130')
