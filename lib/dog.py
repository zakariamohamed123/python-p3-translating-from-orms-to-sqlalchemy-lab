from models import Dog
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def create_table(base, engine):
    base.metadata.create_all(engine)
    

def save(session, dog):
    session.add(dog)
    

def get_all(session):
    return session.query(Dog).all()
    

def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name == name).all()
    for record in query:
        return record
    
    

def find_by_id(session, id):
    find_by_id = session.query(Dog).filter(Dog.id == id).all()
    for record in find_by_id:
        return record

def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name == name, 
        Dog.breed == breed).all()
    for record in query:
        return record

    



def update_breed(session, dog, breed):
    session.query(Dog).update({
        Dog.breed: breed
    })
    
    