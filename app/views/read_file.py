"""Read from file task page"""
from flask import Blueprint, render_template

from app.config import FILES_INPUT_DIR

read_file_bp = Blueprint('read_file', __name__)

@read_file_bp.route('/get-content', endpoint='read_file')
def get_content():
    file_path = FILES_INPUT_DIR.joinpath(".gitkeep")
    try:
        with open(file_path, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        return "File not found", 404

    return render_template('read-file.html', data=data)