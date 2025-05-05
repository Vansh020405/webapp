from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

app = Flask(_name_)
app.secret_key = 'your_secret_key'  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class SearchData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    checkin_date = db.Column(db.String(50), nullable=False)
    checkout_date = db.Column(db.String(50), nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def _repr_(self) -> str:
        return f"{self.id} - {self.location}"

class User(db.Model):
    _tablename_ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)  # Ensure this line is present

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)  

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)  


with app.app_context():
    db.create_all()
    print("Database initialized successfully")


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    print("Request Method:", request.method)
    if request.method == "POST":
        print("POST Request Received")
        email = request.form.get("username")  
        password = request.form.get("password")

        print("Username:", email, "Password:", password)

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session["user"] = email  
            session["user_id"] = user.id 
            print("Login successful, redirecting...")
            return redirect(url_for("user"))  
        else:
            print("Invalid credentials")
            return "Invalid credentials, please try again.", 401

    return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        return render_template("user.html", user=session["user"])
    return redirect(url_for("login")) 


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

      
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "Email already registered. Please log in.", 409

      
        new_user = User(email=email)
        new_user.set_password(password) 
        db.session.add(new_user)
        db.session.commit()

        print("User registered successfully.")
        return redirect(url_for("index"))  

    return render_template("signup.html") 


@app.route("/logout")
def logout():
    session.pop("user", None) 
    return redirect(url_for("index"))


@app.route('/email')
def email():
    return render_template('email.html')

@app.route('/accom')
def accomadation():
    return render_template('accom.html')

@app.route('/homepg')
def homepg():
    return render_template('index.html')


@app.route('/listprop')
def list_properties():
    return render_template('listprop.html')

@app.route('/profile')
def all_login():
    return render_template('profile.html')




@app.route('/search', methods=['POST'])
def search():
    if "user_id" not in session:
        return "You must be logged in to perform a search.", 403  

    location = request.form.get('location')
    checkin_date = request.form.get('checkin_date')
    checkout_date = request.form.get('checkout_date')
    guests = request.form.get('guests')

    user_id = session.get('user_id') 

    new_search = SearchData(
        location=location,
        checkin_date=checkin_date,
        checkout_date=checkout_date,
        guests=int(guests),
        user_id=user_id
    db.session.add(new_search)
    db.session.commit()

    return redirect(url_for('index'))    
 

if _name_ == '_main_':
    app.run(debug=True)
