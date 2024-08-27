from flask import (Blueprint, render_template) 

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    import json

    pets = json.load(open('pets.json'))
    print(pets)

    return render_template('index.html', pets=pets)

