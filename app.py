from flask import Flask, flash, jsonify, redirect, render_template, request, url_for
from sqlalchemy import null
from models import Benefits, Contact, Favourites, Feedback, Smoothies, db
from utils import delete_favourite, initialize_db, toggle_favourite_db

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
    all_favourites_list = Favourites.query.all()    
    all_recid_list = {fav.recid for fav in all_favourites_list}
    return render_template('smoothies.html', smoothies_list = all_smoothies_list, recid_list = all_recid_list)

@app.route('/smoothie-detail/<int:smoothie_id>')
def smoothie_detail(smoothie_id):
    smoothie_detail = Smoothies.query.get_or_404(smoothie_id)    
    return render_template('smoothie_detail.html', smoothie_detail=smoothie_detail)

@app.route('/favourites')
def favourites():
    all_fav_smoothies_list = Smoothies.query.join(Favourites, Smoothies.recid == Favourites.recid).all()
    return render_template('favourites.html', fav_smoothies_list = all_fav_smoothies_list)

@app.route('/toggle_favourite/<int:recid>', methods=['POST'])
def toggle_favourite(recid):
    body = request.get_json()
    in_favourite_val = body['in_favourite'] 
    
    toggle_favourite_db(recid)
    
    new_val = not in_favourite_val
    return jsonify(new_in_favourite=new_val)
    
@app.route('/remove_favourite/<int:recid>')
def remove_favourite(recid):
    delete_favourite(recid)
    return redirect(url_for('favourites'))


@app.route('/remove_all_favourites', methods=['POST'])
def remove_all_favourites():
    try:
        # Delete all records from the Favourites table
        Favourites.query.delete()
        db.session.commit()
        flash('All favourites removed succesfully! Explore more on Smoothie page', 'success')
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while removing favourites.', 'error')
    
    return redirect(url_for('favourites'))
    
@app.route('/contact')
def contact():
    all_feedback_list = Feedback.query.all()
    return render_template('contact.html', feedback_list=all_feedback_list)

@app.route('/contact-list')
def contact_list():
    all_contact_list = Contact.query.all()
    return render_template('contact-list.html', contact_list=all_contact_list)


@app.route('/submit_contact_form', methods=['POST'])
def submit_contact():
    new_name = request.form.get('name')
    new_email = request.form.get('email')
    new_message = request.form.get('message')
    
    new_contact = Contact(name=new_name, email=new_email, message=new_message)
    db.session.add(new_contact)
    db.session.commit()
    
    return redirect(url_for('contact'))    

@app.route('/submit_feedback_form', methods=['POST'])
def submit_feedback():
    new_name = request.form.get('fname')
    new_feedback = request.form.get('feedback')
    
    feedback_obj = Feedback(name=new_name, feedback=new_feedback)
    db.session.add(feedback_obj)
    db.session.commit()
    
    return redirect(url_for('contact'))