from flask import Flask, render_template, request
from models import Benefits, Smoothies, db
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
    all_benefits_list = Benefits.query.all()
    return render_template('benefits.html', benefits_list = all_benefits_list)

@app.route('/smoothies')
def smoothies():
    all_smoothies_list = Smoothies.query.all()
    return render_template('smoothies.html', smoothies_list = all_smoothies_list)

@app.route('/smoothie-detail/<int:smoothie_id>')
def smoothie_detail(smoothie_id):
    smoothie_detail = Smoothies.query.get_or_404(smoothie_id)    
    return render_template('smoothie_detail.html', smoothie_detail=smoothie_detail)

@app.route('/favourites')
def favourites():
    return render_template('favourites.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')