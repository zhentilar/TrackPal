from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=50)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1)])
    height = FloatField('Height (cm)', validators=[DataRequired(), NumberRange(min=0)])
    weight = FloatField('Weight (kg)', validators=[DataRequired(), NumberRange(min=0)])
    daily_calorie_goal = IntegerField('Daily Calorie Goal', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Register')

class FoodEntryForm(FlaskForm):
    name = StringField('Food Name', validators=[DataRequired()])  # Changed from food_name to name
    calories = IntegerField('Calories', validators=[DataRequired()])
    submit = SubmitField('Add Food Entry')