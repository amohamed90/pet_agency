from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class AddPetForm(FlaskForm):

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Image Url")
    age = FloatField("Age")
    notes = StringField("Notes")