# -*- coding: utf-8 -*-
# flask/app.py

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash
from jinja2 import Template
from lookAndSay import lineSeq

app = Flask(__name__)
# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bradzosekretnawartosc',
))

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        odpowiedzi = request.form.to_dict()
        
        if not odpowiedzi["number"] or not odpowiedzi["iterations"]:
            flash("Please, fill required fields",'error')
        else:
            result = lineSeq(odpowiedzi["number"],int(odpowiedzi["iterations"]))
            responseStr=""
            for i in range(len(result)):
                responseStr +=  "<li>#%s: %s</li>" % (i+1, result[i])
                flash(responseStr,'result')
                flash(odpowiedzi["number"], 'number')
                flash(odpowiedzi["iterations"], 'iterations')
        return redirect(url_for('index') )
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
