from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate


from pkg import config
csrf = CSRFProtect()


def create_app():
    """keep all imports that may cause conflict within function so that anytime we write 
    "from pkg.. import.. none of these statements will be executed"""
    from pkg.models import db
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(config.Baseconfig)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    migrate = Migrate(app,db)
    csrf.init_app(app)
    return (app)


app = create_app()
# db
# from flask_sqlalchemy import SQLAlchemy

# instantiating an object of flask

# ensure that the instantiations comes after app has been created or flask has been instantiated.
# load the route
from pkg import admin_route,user_route
from pkg.forms import *