from flask import Flask, render_template, request, redirect
import random
import time

rach=1
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
@app.route("/index",methods=["POST","GET"])
def index():
    if request.method == 'POST':
        print (request.form)
        if request.form['avt_ruc']!=rach:
            rach=request.form['']
    return render_template('ruch.html')


if __name__ == "__main__":
    app.run(debug=True)
