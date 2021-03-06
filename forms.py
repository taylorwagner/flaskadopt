from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, NumberRange, URL, Optional

class AddNewPetForm(FlaskForm):
    """Create form for adding new pets"""
    name = StringField("Pet Name", validators=[InputRequired(message="Pet must have a name")])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired(message="Must select a species for pet")])
    photo_url = StringField("URL of Photo", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Create form for editing pet"""
    photo_url = StringField("URL of Photo", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Availability")