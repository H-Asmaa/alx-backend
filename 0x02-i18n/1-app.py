#!/usr/bin/env python3
"""
0x02. i18n
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """A class Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def hello():
    """A basic flask method."""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
