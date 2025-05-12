from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from .models import Event
from .forms import EventForm
from . import db


main = Blueprint('main', __name__)