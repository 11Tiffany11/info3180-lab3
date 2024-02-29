from flask import Flask
<<<<<<< HEAD
from flask_mail import Mail
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)
from app import views
=======

app = Flask(__name__)
from app import views
>>>>>>> 663996931f8ccecfefc97b886865178a98ef0a03
