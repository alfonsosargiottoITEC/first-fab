import logging ## import de logging

#### imports de flasks
from flask import Flask
from flask_appbuilder import SQLA, AppBuilder



### LOGGING CONFIG ###############
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

######## "ARMAMOS" LA APP #####################
app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session)


######### importamos todas las views ############# debe hacerse al final para evitar circular import
from . import all_views
