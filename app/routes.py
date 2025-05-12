from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from .models import Event
from .forms import EventForm
from . import db


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return redirect(url_for('main.calendar'))


@main.route('/calendar')
def calendar():
    return render_template('calendar.html')


@main.route('/events')
def events():
    events = Event.query.all()
    return jsonify([{
        'id': e.id,
        'title': e.title,
        'start': e.start,
        'end': e.end
    } for e in events])
    
    
@main.route('/event/new', methods=['GET', 'POST'])
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            title=form.title.data,
            start=form.start.data.isoformat(),
            end=form.end.data.isoformat() if form.end.data else None,
            description=form.description.data
        )
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('main.calendar'))
    return render_template('event_form.html', form=form)