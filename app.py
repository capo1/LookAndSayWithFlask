# -*- coding: utf-8 -*-
# flask/app.py

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash
from lookAndSay import lineSeq

app = Flask(__name__)
# konfiguracja aplikacji, w sumie nie wiem póki co, po co to jest,
# było w przykładzie z jakiego korzystałam :shrug:
app.config.update(dict(
    SECRET_KEY='bradzosekretnawartosc',
))

title = "Look and Say - Python Flask Example" 

# główny route aplikacji, obsługujący dwie metody GET i POST
# GET - potrzebny do wyświetlenia
# POST - potrzebny do wysłania danych z formularza
@app.route('/', methods = ['GET', 'POST'])

# Funckja obsługująca wysłanie formularza, bardzo uproszczona
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
            result = lineSeq(odpowiedzi["number"], int(odpowiedzi["iterations"]))
            
            # String z odpowiedzią, rodzielenie logiki odpowiedzi ze sposobem jego wyświetlenia 
            responseStr = ""
            
            # to wyświetla się na consoli
            print(result)
            
            for i in range(len(result)):
                responseStr +=  "<li>#%s: %s</li>" % (i + 1, result[i])
                
            # przypisanie odpowiedzi do stringa result,
            # do którego się odwołuję w componencie result
            # ponieważ używam tutaj HTML'a, w teplecie jest użyte do jego sparsowania "| safe "
            responseStr += '<li><hr/><strong>Sequence:<br/></strong> %s </li>' % ", ".join(result)
            
            # "wysłanie" odpowiedzi do templeta
            flash(responseStr, 'result')
                
            # przypisałam te zmienne do flasha
            # wyświetlane są w ten sam sposób jak result. 
            # Można było przypisać też do GET, 
            # wtedy w url by się wyświetliło:?number=x&iterations=y, 
            # ale nie chciałeś takiego sposobu
            flash(odpowiedzi["number"], 'number')
            flash(odpowiedzi["iterations"], 'iterations')
            
        #przekierowanie do odpowiedniego url'a
        return redirect(url_for('index'))
    
    # wyrenderowanie części templeta, 
    # przekazanie zdefiniowanej zmiennej, tak dla przykładu :)
    return render_template('index.html', title = title)

if __name__ == '__main__':
    app.run(debug=True)