from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assessments.db'

    db.init_app(app)

    # Import routes here to register them after initializing the app
    from .routes import main
    app.register_blueprint(main)

    return app
