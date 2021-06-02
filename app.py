from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddNewPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "santanarush"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def homepage():
    """Show list of pets"""

    pets = Pet.query.all()

    return render_template("index.html", pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Pet add form; handle adding"""

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

        flash(f"Added new pet:{name}!")
        return redirect("/")

    else:
        return render_template(
            "new-pet.html", form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_details(pet_id):
    """Make a page that shows some information about the pet, and It should also show a form that allows us to edit this pet"""

    form = EditPetForm()

    pet = Pet.query.get_or_404(pet_id)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        pet_edits = Pet(photo_url=photo_url, notes=notes, available=available)

        db.session.add(pet_edits)
        db.session.commit()

        flash(f"Edited pet information!")
        return redirect("/{{pet.id}}")

    return render_template('details.html', pet=pet, form=form)