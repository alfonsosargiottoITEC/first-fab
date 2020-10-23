from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

################## EN ESTE BLOQUE TENDRÍA Q IMPORTAR TODAS LAS VIEWS ##################
from app.operators.views import OperatorView, operators_builder # importamos view y builder de operator
##################---------------------------------------------------##################

from . import appbuilder, db



    

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()

