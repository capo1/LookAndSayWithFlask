# -*- coding: utf-8 -*-
# flask/app.py

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash
from lookAndSay import lineSeq

app = Flask(__name__)
# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bradzosekretnawartosc',
))

title = "Look and Say - Python Flask Example" 

# główny roo aplikacji, obsługujący dwie metody GET i POST
# GET potrzebny do wyświetlenia
# POST do wysłania danych z formularza
@app.route('/',methods=['GET', 'POST'])

# Funckja obsługujaca wysłanie formularza. Bardzo uproszczona
def index():
    # Określenie, że żądanie pochodzi z POST'a
    if request.method == 'POST':
        # przypisanie zmiennych z pól formularza do dict
        odpowiedzi = request.form.to_dict()
        
        # podstawowa walidacja formularza
        if not odpowiedzi["number"] or not odpowiedzi["iterations"]:
            flash("Please, fill required fields",'error')
        else:
            # Wykonanie LookAndSay
            result = lineSeq(odpowiedzi["number"],int(odpowiedzi["iterations"]))
            
            # String z odpowiedzią, rodzielenie logiki odpowiedzi ze sposobem jego wyświetlenia 
            responseStr=""
            for i in range(len(result)):
                responseStr +=  "<li>#%s: %s</li>" % (i+1, result[i])
                
                # przypisanie odpowiedzi do stringa result, do którego się odwołuję w componencie result
                flash(responseStr,'result')
                
                # przypisałam te zmienne do flasha, i wyświetlane są w ten sam sposób jak result. Można było przypisać też do GET, wtedy w url by się wyświetliło ?number=x&iterations=y ale nie chciałeś takiego sposobu
                flash(odpowiedzi["number"], 'number')
                flash(odpowiedzi["iterations"], 'iterations')
        #przekierowanie do odpowiedniego url'a
        return redirect(url_for('index') )
    # wyrenderowanie części templeta, przekazanie zdefiniowanej zmiennej
    return render_template('index.html', title = title)

if __name__ == '__main__':
    app.run(debug=True)
