from app import create_app, db

app = create_app()

# Create the database and tables
with app.app_context():
    db.create_all()  # This should ideally be done only once

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development
