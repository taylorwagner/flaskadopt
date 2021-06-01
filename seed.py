from models import db, Pet
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

pet1 = Pet(name="Spike", species="puppy", photo_url="https://images.unsplash.com/photo-1593134257782-e89567b7718a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=375&q=80", age=3, notes="potty-trained", available=True)
pet2 = Pet(name="Duke", species="rooster", age=4, notes="doesn't wake up early")
pet3 = Pet(name="Molly", species="puppy", photo_url="https://images.unsplash.com/photo-1591160690555-5debfba289f0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=400&q=80", available=False)
pet4 = Pet(name="Roger", species="turtle", photo_url="https://images.unsplash.com/photo-1597162216923-ba6d99390c10?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80", age=0, notes="talented", available=False)
pet5 = Pet(name="Mittens", species="kitty", photo_url="https://images.unsplash.com/photo-1529933037705-0d537317ae7b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=371&q=80", age=13)

db.session.add_all([pet1, pet2, pet3, pet4, pet5])

db.session.commit()