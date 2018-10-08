from flask_frozen import Freezer
from server import app


if __name__ == '__main__':
    app.config["FREEZER_DESTINATION"] = "build/open"
    app.config["REGISTRATION_OPEN"] = True
    freezer = Freezer(app)
    freezer.freeze()

    app.config["FREEZER_DESTINATION"] = "build/closed"
    app.config["REGISTRATION_OPEN"] = False
    freezer = Freezer(app)
    freezer.freeze()
