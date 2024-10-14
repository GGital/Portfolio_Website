from flask import Flask, render_template, Response, request, jsonify, session, redirect, url_for, stream_with_context , flash

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio() :
    return render_template('WIP.html')

@app.route('/popgital')
def popgital() :
    return render_template('WIP.html')

@app.route('/info')
def info() :
    return render_template('About_me.html')

if __name__ == '__main__':
    app.run(debug=True , threaded = True)