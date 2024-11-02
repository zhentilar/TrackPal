from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from forms import FoodEntryForm
from models import User, FoodEntry, db
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trackpal.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    target_calories = db.Column(db.Integer, default=2000)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class FoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    target_calories = IntegerField('Target Calories', validators=[DataRequired()])
    submit = SubmitField('Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('home'))
        flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if the username already exists
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('register'))

        # Proceed to create the new user
        new_user = User(username=form.username.data, password_hash=generate_password_hash(form.password.data), target_calories=form.target_calories.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/home')
@login_required
def home():
    print(f"Home route accessed. User authenticated: {current_user.is_authenticated}")
    food_entries = FoodEntry.query.filter_by(user_id=current_user.id).all()
    total_calories = sum(entry.calories for entry in food_entries)
    return render_template('home.html', food_entries=food_entries, total_calories=total_calories)

@app.route('/add_food', methods=['GET', 'POST'])
@login_required
def add_food():
    form = FoodEntryForm()
    if form.validate_on_submit():
        food_entry = FoodEntry(
            name=form.name.data,
            calories=form.calories.data,
            user_id=current_user.id
        )
        db.session.add(food_entry)
        db.session.commit()
        flash('Food entry added successfully!')
        return redirect(url_for('home'))
    return render_template('add_food.html', form=form)

@app.route('/update_target', methods=['GET', 'POST'])
@login_required
def update_target():
    if request.method == 'POST':
        new_target = request.form.get('target_calories', type=int)
        if new_target:
            current_user.target_calories = new_target
            db.session.commit()
            flash('Your calorie target has been updated!', 'success')
            return redirect(url_for('home'))  # Redirect to the user's profile or another relevant page
        else:
            flash('Please enter a valid number for the calorie target.', 'danger')
    
    return render_template('update_target.html')  # Create a corresponding HTML template

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(port=8000, debug=True)
