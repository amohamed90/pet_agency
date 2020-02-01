from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, ValidationError

def species_check(form, field):
    result = (field.data == "Dog" or field.data == "Cat" or field.data == "Porcupine")
    if (not result):
        raise ValidationError("Not a correct species")
    return result

def age_check(form, field):
    return (field.data >= 0 or field.data <= 30)

class AddPetForm(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices = [("Dog", "Dog"), ("Cat", "Cat"), ("Porcupine", "Porcupine")] ,validators=[InputRequired(), species_check])
    photo_url = StringField("Image Url", validators=[Optional(),URL()])
    age = FloatField("Age", validators=[InputRequired(), age_check])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")

class EditPetForm(FlaskForm):

    photo_url = StringField("Image Url", validators=[Optional(),URL()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")