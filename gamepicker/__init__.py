"""
PROJECT: GAMEPICKER

An advanced toolkit for selecting Loto-Québec games

For Windows cmd:

> set FLASK_APP=gamepicker
> set FLASK_ENV=development
> flask run

For Windows PowerShell, use $env: instead of set:

> $env:FLASK_APP = "gamepicker"
> $env:FLASK_ENV = "development"
> flask run

For Linux and Mac, use export instead of set:

$ export FLASK_APP=gamepicker
$ export FLASK_ENV=development
$ flask run

You’ll see output similar to this:

* Serving Flask app "gamepicker"
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761

Visit http://127.0.0.1:5000/hello in a browser and you should see the “Hello, World!” message.

"""

__version__ = "0.0.0"
__author__ = "Alain Rouleau"
__copyright__ = "Copyright © 2021 Alain Rouleau. All rights reserved."

from flask import Flask

# Application Factory
def create_app():
    """ Create and configure the app """

    app = Flask(__name__)

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    return app
