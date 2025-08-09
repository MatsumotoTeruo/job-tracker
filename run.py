from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
# Cuối file run.py
with app.app_context():
    from app import db
    db.create_all()
