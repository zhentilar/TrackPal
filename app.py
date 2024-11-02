from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from forms import FoodEntryForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trackpal.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Specify what page to load for non-authenticated users

# Your existing models and forms here...

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
        user = User(username=form.username.data, target_calories=form.target_calories.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(port=8000, debug=True)