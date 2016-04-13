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
