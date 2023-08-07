"""Generate user page"""

from flask import Blueprint, render_template
from app.services import generate_users_task

generate_users_bp = Blueprint('generate_users', __name__)

@generate_users_bp.route('/generate-users')
@generate_users_bp.route('/generate-users/<int:count>')
def generate_users(count: int = 30):
    """Generate user - route"""
    return render_template('generate-users.html', users=generate_users_task.generate_users(count))