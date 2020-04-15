# -*- coding: utf-8 -*-
# flask/app.py

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash

from lookAndSay import lineSeq

app = Flask(__name__)
# Konfiguracja aplikacji, w sumie nie wiem póki co, po co to jest,
# było w przykładzie z jakiego korzystałam :shrug:
app.config.update(dict(
    SECRET_KEY='bradzosekretnawartosc',
))

title = "Look and Say - Python Flask Example" 

# główny route aplikacji, obsługujący dwie metody GET i POST
# GET - potrzebny do wyświetlenia
# POST - potrzebny do wysłania danych z formularza
@app.route('/', methods = ['GET', 'POST'])

# Funkcja obsługująca wysłanie formularza, bardzo uproszczona
def index():
    # Określenie, że żądanie pochodzi z POST'a
    if request.method == 'POST':
        
        # przypisanie zmiennych z pól formularza do dict
        odpowiedzi = request.form.to_dict()
        
        # podstawowa walidacja formularza
        if not odpowiedzi["number"] or not odpowiedzi["iterations"]:
            flash("Please, fill required fields", 'error')
        else:
            # Wykonanie LookAndSay
            results = lineSeq(odpowiedzi["number"], int(odpowiedzi["iterations"]))
            
        #przekierowanie do odpowiedniego url'a
        return render_template('index.html', title = title, results = results, inputs = {"number": odpowiedzi["number"], 'iterations': odpowiedzi["iterations"]})
    
    # wyrenderowanie części templeta, 
    # przekazanie zdefiniowanej zmiennej, tak dla przykładu :)
    return render_template('index.html', title = title, inputs = {"number": 5, 'iterations': 10} )

if __name__ == '__main__':
    app.run(debug = True)