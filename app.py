from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddNewPetForm

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


@app.route('/add')
def add_pet():

    form = AddNewPetForm()

    return render_template('new-pet.html', form=form)