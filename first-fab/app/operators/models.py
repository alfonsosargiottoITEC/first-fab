
from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from app import db

class Operator(Model):
    idOperator = db.Column(db.Integer, primary_key=True)
    nameOperator = db.Column(db.String(50), nullable=False)
    birthdateOperator = db.Column(db.String(50), nullable=False)
    emailOperator = db.Column(db.String(150), nullable=False)
    activeOperator = db.Column(db.Boolean(1))
    
    def __repr__(self):
        return self.nameOperator,self.birthdateOperator, self.emailOperator, self.activeOperator
