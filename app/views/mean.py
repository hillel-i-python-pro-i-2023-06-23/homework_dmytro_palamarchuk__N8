"""Mean page"""

from flask import Blueprint, render_template

from app.services import utils
from app.services.average_value_task import calculate_avg_value_from_people_csv_data, get_data_from_google_drive

mean_bp = Blueprint('mean', __name__)

@mean_bp.route('/mean')
def mean():
    height, weight = calculate_avg_value_from_people_csv_data(
        get_data_from_google_drive()
    )

    return render_template(
        'mean.html',
        height = round(utils.inches_to_cm(height), 2),
        weight = round(utils.pounds_to_kg(weight), 3),
    )