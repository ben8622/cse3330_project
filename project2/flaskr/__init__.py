import os

from flask import Flask
from flask_navigation import Navigation
from flask.templating import render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    nav = Navigation(app)

    nav.Bar('top', [
        nav.Item('Home', 'index'),
        nav.Item('Assignment', 'assignment')
    ])

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import assignment
    app.register_blueprint(assignment.bp)

    @app.route('/', methods=['GET'])
    def home():
        return render_template('/home.html')

    return app