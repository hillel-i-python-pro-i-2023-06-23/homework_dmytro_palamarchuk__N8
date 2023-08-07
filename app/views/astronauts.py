"""Astronauts page"""

from flask import Blueprint, render_template
from app.services.astronauts_task import get_astronauts, get_station_astronauts

astronauts_bp = Blueprint('astronauts', __name__)

@astronauts_bp.route('/space')
def astronauts():
    data = get_astronauts()
    number = data['number']
    stations = get_station_astronauts(data['people'])
    return render_template(
        'astronauts.html',
        number = number,
        stations = stations,
    )