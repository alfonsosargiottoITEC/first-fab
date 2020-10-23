from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from app import appbuilder
####################
from app.operators.models import Operator ####### import del MODEL de operator
###########



# clase para armar el modelo
class OperatorView (ModelView):
    datamodel = SQLAInterface(Operator) # de donde traemos el modelo, supongo
    label_columns = {'nameOperator':'Nombre', 'birthdateOperator':'Fecha de nacimiento', 'emailOperator':'E-mail', 'activeOperator':'¿Activo?'} # estructura -> 'nombreAtributoModel':'nombre_a_Mostrar_en_Columna'

    list_columns = ["nameOperator", "birthdateOperator", "emailOperator", "activeOperator"] #lista de columnas a mostrar en el listado

    # lista de campos y atributos a mostrar en el "show" de cada registro
    show_fieldsets =[
        ('Resumen',{'fields': ['nameOperator', 'emailOperator','activeOperator']}
        ),
        ('Información personal ',{'fields': ['nameOperator', 'birthdateOperator', 'emailOperator']}
        ),
        ]
    #campos a mostrar en el CREATE de un nuevo registro
    add_fieldsets = [
        ("Informacion Basica", {"fields": ["nameOperator", "emailOperator","birthdateOperator", "activeOperator"]})
    ]

# esto es para registrar la vista?
operators_builder = appbuilder.add_view(
    OperatorView,
    "CRUD Operators",
    icon = "fa-folder-open-o",
    category = "Operators",
    category_icon = "fa-envelope"
)
