from flask import Blueprint, render_template
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "<h1>Hello from Flask!</h1>"
