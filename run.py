# run.py – point d’entrée dev; gunicorn/uwsgi pour prod
from app import app

if __name__ == "__main__":
    # debug=True => autoreload + trace, parfait pour dev
    app.run(debug=True, host="0.0.0.0", port=5000)
