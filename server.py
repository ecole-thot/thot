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
REGISTRATION_LINKS = {
  "fr" : "https://docs.google.com/forms/d/1guNbmsJMf5zuIfXOI29gk2PAZW4Q7jN_AMakHbQWuNY/prefill",
  "en" : "https://docs.google.com/forms/d/1wiG256MUSOQWaz9sO-3xdVXoLdnNRVqZD4kUZQnO3Zc/prefill",
  "ar" : "https://docs.google.com/forms/d/1qlQXouDwlkJ5JRzouFPW5MTRqf8_XWjSMtHOj6MrlXA/prefill",
  "ps" : "https://docs.google.com/forms/d/1u1p4ECm6yTmwISX_2e3Os5K3TretWZFEtKMFjUbOwrU/prefill",
  "fa" : "https://docs.google.com/forms/d/1IyexQfwISQn5uezndVyHWYNR4gqUQe3lsuv3Iqts6Pg/prefill"
}
VOLUNTEER_OPEN = True
VOLUNTEER_LINK = "https://docs.google.com/forms/d/1wiG256MUSOQWaz9sO-3xdVXoLdnNRVqZD4kUZQnO3Zc/prefill"
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
      "text": "Le but de l’association Thot est que les réfugiés fassent partie de la France"
    },
    { "link": "https://rcf.fr/actualite/journal-regional-du-mardi-26-avril",
      "title": "RCF",
      "text": "Journal Régional — 1'36\""
    },
    { "link": "http://cheekmagazine.fr/societe/thot-judith-aquien-ecole-francais-refugies/",
      "title": "Cheek Magazine",
      "text": "Elle a quitté son job pour créer Thot, une école de français destinée aux réfugiés (29/04/2016)"
    },
    { "link": "http://bit.ly/1QPVrPj",
      "title": "One Heart",
      "text": "Thot, une école pour les réfugiés à soutenir sur Ulule (29/04/2016)"
    },
    { "link": "http://www.integrales-productions.com/2016/04/30/thot-lecole-diplomante-de-francais-pour-eleves-en-migration/",
      "title": "Intégrales Mag",
      "text": "Thot, l’école diplomante de français pour élèves en migration (30/04/2016)"
    },
    { "link": "http://www.novaplanet.com/radionova/60626/episode-projet-thot",
      "title": "Le futur c'est maintenant, Nova",
      "text": "Chronique de Côme Bastin sur Thot (30/04/2016)"
    },
    { "link": "http://bit.ly/1SVONvB",
      "title": "Cosmopolitaine, France Inter",
      "text": "Chronique de Marie-Madeleine Rigopoulos sur Thot - 26'30\" (01/05/2016)"
    },
    { "link": "http://annieallmusic.blogspot.fr/2016/05/thot-un-grand-pas-vers-lintegration.html",
      "title": "Annie All Music",
      "text": "Thot, un grand pas vers l'intégration (02/05/2016)"
    },
    { "link": "http://2016.wetalk-community.org/modeles-feminins/",
      "title": "W(e) Talk",
      "text": "Judith Aquien, Présidente de Thot, sélectionnée parmi les 8 modèles féminins 2016, à la conférence \"Artisanes du commun, qui forment ensemble pour un autre demain\" du 21 mai 2016"
    },
    { "link": "http://issuu.com/lcf-magazine/docs/lcff_magazine_n__40-_issuu/43?e=6017579/35344828",
      "title": "Langue et culture françaises & francophones",
      "text": "Le magazine LCFF nous offre une page de publicité (numéro 40, mai 2016)"
    },
    { "link": "http://www.france4.fr/emissions/l-autre-jt/videos/replay_-_lautre_jt_05-05-2016_1142885",
      "title": "L'Autre JT",
      "text": "Sarah Constantin met 20/20 à Thot - 20'24'' (05/05/2016)"
    },
    { "link": "https://www.youtube.com/watch?v=KqqYWuFPRpE&feature=youtu.be",
      "title": "LCI",
      "text": "Thot invité au journal de midi (5/05/2016)"
    },
    { "link": "http://www.novaplanet.com/radionova/bientot-2h-14-avant-la-fin-du-monde-thot-la-formation-qui-apprend-le-francais-aux-refugies",
      "title": "Nova - 2h 1/4 avant la fin du monde",
      "text": "Judith Aquien invitée de Marie Misset et Armel Hemme (09/05/2016)"
    },
    { "link": "http://www.clique.tv/thot-lecole-diplomante-pour-les-refugies/",
      "title": "Clique.tv",
      "text": "Thot, l’école diplômante pour les réfugiés qui veulent apprendre le français (11/05/2016)"
    },
    { "link": "http://pressee.fr/judith-aquien-il-faut-transmettre-un-horizon-aux-refugies/#more-898",
      "title": "Pressée",
      "text": "« Avec Thot, on transmet un horizon aux réfugiés. » (11/05/2016) "
    },
    { "link": "https://savoir.actualitte.com/article/scolarite/1798/du-crowdfunding-pour-creer-une-ecole-apprenant-le-francais-aux-refugies",
      "title": "Actualitté",
      "text": "Du crowdfunding pour créer une école apprenant le français aux réfugiés (13/05/2016)"
    },
    { "link": "http://www.liberation.fr/debats/2016/05/02/ils-ferment-les-frontieres-ouvrons-nos-ecoles_1450031",
      "title": "Libération",
      "text": "\"Ils ferment les frontières, ouvrons nos écoles\" - tribune du Résome dans Libération 2/05/2016"
    },
    { "link": "http://www.rfi.fr/emission/20160418-institut-francais-bucarest",
      "title": "RFI",
      "text": "Chronique « Ma Parole » : Interview d'Imaad Ali, directeur pédagogique de l'école Thot - 17'55 RFI 18/04/16"
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
        registration_links=REGISTRATION_LINKS,
        registration_open=REGISTRATION_OPEN,
        volunteer_link=VOLUNTEER_LINK,
        volunteer_open=VOLUNTEER_OPEN,
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
