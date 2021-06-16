from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddNewPetForm, EditPetForm
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///adopt')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'hellosecret1')
print('************************')
print('************************')
print('************************')
print(app.config["SECRET_KEY"])
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def homepage():
    """Show list of all pets and whether they are available or not"""

    pets = Pet.query.all()

    return render_template("index.html", pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add a new pet form; handle adding of new pet"""

    form = AddNewPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added new pet: {name}!")
        return redirect("/")

    else:
        return render_template(
            "new-pet.html", form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_details(pet_id):
    """Make a page that shows some information about an individual pet, and the page should also show a form that allows edits of pet"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f"Edited pet information!")
        return redirect(f"/{pet.id}")

    return render_template('details.html', pet=pet, form=form)