from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index():
    # return render_template('test.html')
    print(request.args.get('age', 1, int))
    return 'hello world!'


if __name__ == '__main__':
    app.run(host='192.168.196.130')
