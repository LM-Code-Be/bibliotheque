# app.py – adapté pour PyMySQL
from flask import Flask
from flask_mysqldb import MySQL
from config import Config
from controllers.book_controller import book_bp
from models.book_model import BookModel
import controllers.book_controller as book_controller

mysql = MySQL()                           # même logique qu’avant

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    mysql.init_app(app)                   # initialisation PyMySQL

    model = BookModel(mysql)
    book_controller.model = model

    app.register_blueprint(book_bp)
    return app

app = create_app()
