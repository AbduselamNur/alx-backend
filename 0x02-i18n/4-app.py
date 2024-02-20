#!/usr/bin/env python3
"""Force locale with URL parameter"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False


@babel.localeselector
def get_locale() -> str:
    """ GET locale
    Return: Detect the best match for the supported languages
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ GET /
    Return: 4-index.html
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
