from flask import Flask, render_template
from models import db
from utils import initialize_db

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

with app.app_context():
    db.create_all()
    initialize_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/benefits')
def benefits():
    return render_template('benefits.html')

@app.route('/smoothies')
def smoothies():
    return render_template('smoothies.html')

@app.route('/favourites')
def favourites():
    return render_template('favourites.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')