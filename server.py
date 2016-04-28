# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, render_template, request
from flask.ext.babel import Babel

app = Flask(__name__)
app.config.update(
    BABEL_DEFAULT_LOCALE='fr_FR',
    BABEL_DEFAULT_TIMEZONE='Europe/Paris')
babel = Babel(app)


DONATION_LINK = "https://fr.ulule.com/ecole-thot/"
REGISTRATION_OPEN = False
REGISTRATION_LINK = "##"
BUDGET_AVAILABLE = False
NB_STUDENTS = 0

PRESS = [
    { "link": "https://savoirs.rfi.fr/fr/communaute/langue-francaise/ma-parole-on-vous-presente-thot",
      "title": "RFI — Émission « Danse avec les mots »",
      "text": "Chronique « Ma Parole » : on vous présente Thot"
    },
    { "link": "http://www.liberation.fr/direct/element/une-ecole-pour-migrants-gratuite-et-diplomante-pourrait-voir-le-jour-en-france_35401/",
      "title": "Libération",
      "text": "Une école pour migrants gratuite et diplômante pourrait voir le jour en France (18/04/2016)"
    },
    { "link": "http://agi.to/agitox-actualite-fle-edu-76/",
      "title": "Agito", 
      "text": "Thot FLE, une école diplômante pour migrants"
    },
    { "link": "http://consocollaborative.com/article/elles-lancent-une-ecole-de-francais-pour-les-refugies-grace-au-crowdfunding/",
      "title": "Conso Collaborative",
      "text": "Elles lancent une école de français pour les réfugiés"
    },
    { "link": "http://www.lecourrier-du-soir.com/articles/h%C3%A9lo%C3%AFse-%C2%AB-le-de-l%E2%80%99association-thot-est-que-les-r%C3%A9fugi%C3%A9s-fassent-partie-de-la-france-%C2%BB",
      "title": "Le Courrier du Soir", 
      "text": "le but de l’association Thot est que les réfugiés fassent partie de la France"
    },
    { "link": "https://rcf.fr/actualite/journal-regional-du-mardi-26-avril",
      "title": "RCF",
      "text": "Journal Régional — 1'36\""
    }
]

@babel.localeselector
def get_locale():
    # if a user is logged in, use the locale from the user settings
    locale = getattr(request, 'locale', None)
    if locale is not None:
        return locale
    return 'fr'


def render_home():
    return render_template(
        'home.html',
        donation_link=DONATION_LINK,
        registration_link=REGISTRATION_LINK,
        registration_open=REGISTRATION_OPEN,
        budget_available=BUDGET_AVAILABLE,
        nb_students=NB_STUDENTS,
        press=PRESS,
        locale=request.locale)


@app.route('/')
def homepage_fr():
    request.locale = 'fr'
    return render_home()


@app.route('/en.html')
def homepage_en():
    request.locale = 'en'
    return render_home()


@app.route('/ar.html')
def homepage_ar():
    request.locale = 'ar'
    return render_home()


@app.route('/ps.html')
def homepage_ps():
    request.locale = 'ps'
    return render_home()


@app.route('/fa.html')
def homepage_fa():
    request.locale = 'fa'
    return render_home()


if __name__ == '__main__':
    app.run(port=8080, debug=True)
