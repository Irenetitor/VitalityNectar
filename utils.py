
import csv
from config import RESOURCE_SMOOTHIES
from models import Smoothies, db


def initialize_db():
    delete_all_smoothies()
    insert_all_smoothies(RESOURCE_SMOOTHIES)
    
def delete_all_smoothies():
    Smoothies.query.delete()
    db.session.commit()
    
def insert_all_smoothies(csv_file):
    with open(csv_file, 'r') as f:
        
        reader = csv.DictReader(f)
        
        for row in reader:
            item = Smoothies(
                recid=row['recid'],
                recipename=row['recipename'],
                description=row['description'],
                ingredients=row['ingredients'],
                image=row['image'])
            print(item)
            db.session.add(item)
            
    db.session.commit()
    
    
       
    
    