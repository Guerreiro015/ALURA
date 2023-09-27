from flask import Flask

app = Flask(__name__)

app.config.from_prefixed_env()
app.config["SECRET_KEY"] = "5f352379324c22463451387a0aec5d2f"
from app import site_teste