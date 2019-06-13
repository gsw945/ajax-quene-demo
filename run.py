import random

from flask import Flask, render_template, jsonify,  make_response

app = Flask(__name__)

@app.route('/robots.txt')
@app.route('/favicon.ico')
def view_favicon():
    return make_response('', 204)

@app.route('/')
def view_index():
    return render_template('index.html')

@app.route('/ajax', methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH'])
def view_ajax():
    delay = random.random() * 5
    import time; time.sleep(delay)
    return jsonify({'error': 0, 'desc': '成功', 'data': delay})

if __name__ == '__main__':
    cfg = dict(
        host='127.0.0.1',
        port=8787,
        debug=True
    )
    app.run(**cfg)
