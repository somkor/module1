from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class UniqueDigitsForm(FlaskForm):
    number = IntegerField('введіть ціле позитивне число:', validators=[
        DataRequired(message="це поле не може бути порожнім"),
        NumberRange(min=1, message="будь ласка, введіть позитивне число")
    ])
    submit = SubmitField('перевірити')
