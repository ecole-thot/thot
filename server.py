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


DONATION_LINK = "https://thot-transmettre-un-horizon-a-tous.donnerenligne.fr/"
REGISTRATION_OPEN = False
REGISTRATION_LINKS = {
  "fr" : "https://docs.google.com/forms/d/1guNbmsJMf5zuIfXOI29gk2PAZW4Q7jN_AMakHbQWuNY",
  "en" : "https://docs.google.com/forms/d/1cSZY4Cx4j_DysueON7yER2GGxn1HpQov52tjEOudCqo",
  "ar" : "https://docs.google.com/forms/d/1qlQXouDwlkJ5JRzouFPW5MTRqf8_XWjSMtHOj6MrlXA",
  "ps" : "https://docs.google.com/forms/d/1u1p4ECm6yTmwISX_2e3Os5K3TretWZFEtKMFjUbOwrU",
  "fa" : "https://docs.google.com/forms/d/1IyexQfwISQn5uezndVyHWYNR4gqUQe3lsuv3Iqts6Pg"
}
VOLUNTEER_OPEN = False
VOLUNTEER_LINK = "https://docs.google.com/forms/d/1wiG256MUSOQWaz9sO-3xdVXoLdnNRVqZD4kUZQnO3Zc"
BUDGET_AVAILABLE = False
NB_STUDENTS = 40

PRESS = [
    { "link": "https://savoirs.rfi.fr/fr/communaute/langue-francaise/ma-parole-on-vous-presente-thot",
      "title": "RFI — Émission « Danse avec les mots »",
      "text": "Chronique « Ma Parole » : on vous présente Thot (11/04/2016)"
    },
    { "link": "http://www.liberation.fr/direct/element/une-ecole-pour-migrants-gratuite-et-diplomante-pourrait-voir-le-jour-en-france_35401/",
      "title": "Libération",
      "text": "Une école pour migrants gratuite et diplômante pourrait voir le jour en France (18/04/2016)"
    },
    { "link": "http://www.rfi.fr/emission/20160418-institut-francais-bucarest",
      "title": "RFI",
      "text": "Chronique « Ma Parole » : Interview d'Imaad Ali, directeur pédagogique de l'école Thot - 17'55 (18/04/16)"
    },
    { "link": "http://agi.to/agitox-actualite-fle-edu-76/",
      "title": "Agito", 
      "text": "Thot FLE, une école diplômante pour migrants (22/04/2016)"
    },
    { "link": "http://consocollaborative.com/article/elles-lancent-une-ecole-de-francais-pour-les-refugies-grace-au-crowdfunding/",
      "title": "Conso Collaborative",
      "text": "Elles lancent une école de français pour les réfugiés (26/04/2016)"
    },
    { "link": "https://rcf.fr/actualite/journal-regional-du-mardi-26-avril",
      "title": "RCF",
      "text": "Journal Régional — 1'36\" (26/04/2016)"
    },
    { "link": "http://www.lecourrier-du-soir.com/articles/h%C3%A9lo%C3%AFse-%C2%AB-le-de-l%E2%80%99association-thot-est-que-les-r%C3%A9fugi%C3%A9s-fassent-partie-de-la-france-%C2%BB",
      "title": "Le Courrier du Soir", 
      "text": "Le but de l’association Thot est que les réfugiés fassent partie de la France (27/04/2016)"
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
    { "link": "http://www.novaplanet.com/radionova/61238/episode-thot-la-formation-qui-apprend-le-francais-aux-refugies",
      "title": "Le futur c'est maintenant, Nova",
      "text": "Chronique de Côme Bastin sur Thot (30/04/2016)"
    },
    { "link": "http://bit.ly/1SVONvB",
      "title": "Cosmopolitaine, France Inter",
      "text": "Chronique de Marie-Madeleine Rigopoulos sur Thot - 26'30\" (01/05/2016)"
    },
    { "link": "http://issuu.com/lcf-magazine/docs/lcff_magazine_n__40-_issuu/43?e=6017579/35344828",
      "title": "Langue et culture françaises & francophones",
      "text": "Le magazine LCFF nous offre une page de publicité (numéro 40, mai 2016) (01/05/2016)"
    },
    { "link": "http://annieallmusic.blogspot.fr/2016/05/thot-un-grand-pas-vers-lintegration.html",
      "title": "Annie All Music",
      "text": "Thot, un grand pas vers l'intégration (02/05/2016)"
    },
    { "link": "http://www.liberation.fr/debats/2016/05/02/ils-ferment-les-frontieres-ouvrons-nos-ecoles_1450031",
      "title": "Libération",
      "text": "\"Ils ferment les frontières, ouvrons nos écoles\" - tribune du Résome dans Libération (02/05/2016)"
    },
    { "link": "http://www.france4.fr/emissions/l-autre-jt/videos/replay_-_lautre_jt_05-05-2016_1142885",
      "title": "L'Autre JT",
      "text": "Sarah Constantin met 20/20 à Thot - 20'24'' (05/05/2016)"
    },
    { "link": "http://www.telerama.fr/monde/le-resome-pour-que-l-ecole-accueille-les-refugies-dans-la-dignite,141947.php",
      "title": "Télérama",
      "text": "Le Resome, pour que l’école accueille les réfugiés dans la dignité (05/05/2016)"
    },
    { "link": "https://www.youtube.com/watch?v=KqqYWuFPRpE&feature=youtu.be",
      "title": "LCI",
      "text": "Thot invité au journal de midi (05/05/2016)"
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
      "text": "« Avec Thot, on transmet un horizon aux réfugiés. » (11/05/2016)"
    },
    { "link": "http://www.redattoresociale.it/Notiziario/Articolo/507633/In-Francia-apre-Thot-scuola-di-francese-per-richiedenti-asilo-e-rifugiati",
      "title": "Redattore Sociale",
      "text": "In Francia apre “Thot”, scuola di francese per richiedenti asilo e rifugiati (11/05/2016)"
    },
    { "link": "https://savoir.actualitte.com/article/scolarite/1798/du-crowdfunding-pour-creer-une-ecole-apprenant-le-francais-aux-refugies",
      "title": "Actualitté",
      "text": "Du crowdfunding pour créer une école apprenant le français aux réfugiés (13/05/2016)"
    },
    { "link": "http://www.lecourrierdelatlas.com/1138518052016Une-ecole-pour-apprendre-le-francais-aux-refugies.html",
      "title": "Le Courrier de l'Atlas",
      "text": "\"Une école pour apprendre le français aux réfugiés\" (18/05/2016)"
    },
    { "link": "http://www.letudiant.fr/jobsstages/creation-entreprise/heloise-nio-25-ans-cofondatrice-d-une-ecole-pour-former-les-exiles-a-la-langue-francaise.html",
      "title": "L'Etudiant",
      "text": "Héloïse a cofondé une école pour former les exilés à la langue française (19/05/2016)"
    },
    { "link": "http://www.leparisien.fr/montreuil-93100/montreuil-elles-veulent-creer-une-ecole-de-francais-pour-les-refugies-19-05-2016-5810251.php",
      "title": "Le Parisien",
      "text": "Elles veulent créer une école de français pour les réfugiés (19/05/2016)"
    },
    { "link": "http://www.lepoint.fr/societe/thot-l-ecole-qui-apprend-le-francais-aux-refugies-20-05-2016-2040741_23.php",
      "title": "Le Point",
      "text": "Thot, l'école qui apprend le français aux réfugiés (20/05/2016)"
    },
    { "link": "http://www.lexpress.fr/actualites/1/styles/a-paris-une-ecole-des-refugies-pour-apprendre-le-francais_1794126.html",
      "title": "L’Express via l’AFP",
      "text": "A Paris, une \"école des réfugiés\" pour apprendre le français (20/05/2016)"
    },
    { "link": "http://tempsreel.nouvelobs.com/societe/20160520.AFP5837/a-paris-une-ecole-des-refugies-pour-apprendre-le-francais.html",
      "title": "L'Obs",
      "text": "A Paris, une \"école des réfugiés\" pour apprendre le français (20/05/2016)"
    },
    { "link": "http://2016.wetalk-community.org/modeles-feminins/",
      "title": "W(e) Talk",
      "text": "Judith Aquien, Présidente de Thot, sélectionnée parmi les 8 modèles féminins 2016, à la conférence \"Artisanes du commun, qui forment ensemble pour un autre demain\" (21/05/2016)"
    },
    { "link": "http://lapartducolibri.fr/?p=837",
      "title": "La Part du colibri",
      "text": "Une école diplômante pour apprendre le français aux réfugiés (23/05/2016)"
    },
    { "link": "https://www.mediapart.fr/journal/france/260516/migrants-comment-aider",
      "title": "Mediapart",
      "text": "Migrants: comment aider? (26/05/2016)"
    },
    { "link": "http://www.franceculture.fr/emissions/rue-des-ecoles/rue-des-ecoles-dimanche-29-mai-2016",
      "title": "France Culture (\"Rue des écoles\")",
      "text": "Focus : \"Thot, une école pour les migrants\", avec Judith Aquien, présidente de Thot à 48' (29/05/2016)"
    },
    { "link": "http://www.lesinrocks.com/2016/05/31/actualite/12-femmes-bousculer-quotidien-11826880/",
      "title": "Les Inrocks",
      "text": "12 femmes qui vont bousculer votre quotidien (31/05/2016)"
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
