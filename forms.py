from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional, URL, ValidationError

def species_check(form, field):
    print("////////////////////////////////////",field.data)
    result = (field.data == "dog" or field.data == "cat" or field.data == "porcupine")
    print(result)
    if (not result):
        raise ValidationError("Not a correct species")
    return result

def age_check(form, field):
    return (field.data >= 0 or field.data <= 30)

class AddPetForm(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), species_check])
    photo_url = StringField("Image Url", validators=[Optional(),URL()])
    age = FloatField("Age", validators=[InputRequired(), age_check])
    notes = StringField("Notes", validators=[Optional()])


