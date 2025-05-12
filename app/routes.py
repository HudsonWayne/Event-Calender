from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from .models import Event
from .forms import EventForm
from . import db


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return redirect(url_for('main.calendar'))