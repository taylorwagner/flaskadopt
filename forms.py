from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class AddNewPetForm(FlaskForm):
    """Create form for adding new pets"""
    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("URL of Photo")
    age = FloatField("Age")
    notes = StringField("Notes")