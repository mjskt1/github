from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return render_template('test.html')
    # return 'hello world!'
    response = make_response('index')
    response.status_code  = 250
    response.headers['name'] = 'laowang01'
    return response
if __name__ == '__main__':
    app.run(host='192.168.196.130')
