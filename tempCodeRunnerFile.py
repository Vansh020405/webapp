from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for storing search data
class SearchData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    checkin_date = db.Column(db.String(50), nullable=False)
    checkout_date = db.Column(db.String(50), nullable=False)
    guests = db.Column(db.Integer, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to render the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/search', methods=['POST'])
def search():
    location = request.form.get('location')
    checkin_date = request.form.get('checkin_date')
    checkout_date = request.form.get('checkout_date')
    guests = request.form.get('guests')

    # Save data to the database
    new_search = SearchData(location=location, checkin_date=checkin_date, checkout_date=checkout_date, guests=int(guests))
    db.session.add(new_search)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
