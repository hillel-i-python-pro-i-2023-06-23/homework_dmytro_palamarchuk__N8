"""Entry point"""
from flask import Flask
from dotenv import load_dotenv

from app.config import ROOT_DIR
from app.loggers.init_logging import init_logging
from app.views.home import home_bp
from app.views.read_file import read_file_bp
from app.views.generate_users import generate_users_bp
from app.views.astronauts import astronauts_bp
from app.views.mean import mean_bp

app = Flask(__name__)

app.root_path = ROOT_DIR.joinpath("app")

app.register_blueprint(home_bp)
app.register_blueprint(read_file_bp)
app.register_blueprint(generate_users_bp)
app.register_blueprint(astronauts_bp)
app.register_blueprint(mean_bp)

if __name__ == "__main__":
    # Upload dotenv configuration
    load_dotenv()
    # Initialize logging
    init_logging()

    app.run(host="0.0.0.0", port=5000, debug=True)
