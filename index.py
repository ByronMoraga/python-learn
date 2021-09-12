# TUTORIAL PYTHON-WEB
# console: pip install Flask
from flask import Flask, render_template
import flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)#debug=True indica que es modo de prueba

# Run in consola 'cd PYTHON-WEBSITE' -> python index.py

# subir a la nube
# https://www.heroku.com/
# Crear entorno virtual
# console: pip install virtualenv

# console: python -m venv venv

# console: cd venv/Scripts
# instalarle flask
# console: pip install Flask
# python ../../src/index.py 

# instalar heroku cli
# console: heroku --version
# console: heroku login

# console: pip install gunicorn

# utilizar en procfile
# archivos txt  
# -buscar heroku python runtime

# console: pip freeze > ../../requirements.txt

# Instalar git for visual studio code
# console:
#  cd src
#  git init
#  git add .
#  git status
# configurar git ------------->
# git config user.name "byron"
# git config user.email byron_moraga@hotmail.com
# -----------------------------
# git commit -m "primera subida a heroku"
# heroku create python-app-byron
# heroku git:remote python-app-byron
# git push heroku master
