from flask import Flask, render_template, request
#from  import SQLAlchemy
import requests

app = Flask(__name__)


# When form is not yet accessed
@app.route('/')
def func():
    return render_template("input.html")


# When form is accessed
@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
         url_ = request.form['url']
         try:
             resp = requests.get(url_)
             count = len(resp.text.split())
             return render_template("docfile.html", text=url_, number=count)
         except requests.exceptions.ConnectionError:
             return '<h3>Connection refused</h3>'


if __name__ == '__main__':
    app.run()
