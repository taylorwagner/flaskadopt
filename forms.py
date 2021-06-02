from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, RadioField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddNewPetForm(FlaskForm):
    """Create form for adding new pets"""
    name = StringField("Pet Name", validators=[InputRequired()])
    species = RadioField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired()])
    photo_url = StringField("URL of Photo", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Create form for editing pet"""
    photo_url = StringField("URL of Photo", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Availability")