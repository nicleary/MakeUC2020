import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from . import db

bp = Blueprint('report', __name__, url_prefix='/report')

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        flags = [0 for x in range(32)]
        num_criteria = 10

        for i in range(num_criteria): 
            radio_str = 'criteria_' + str(i) + '_radio' # TODO Make this match the naming convention for the selector
            flag = int(request.form[radio_str])
            if flag == 0: # Negative
                flags[x] = 1
            elif flag == 2: # Positive
                flags[x + 16] = 1
        
        flags_out = 0
        for x in enumerate(flags):
            flags_out += x[1] << x[0]

        report_text = request.form['textbox']

        user = conn.execute(
            'INSERT INTO reports (UID, LID, TIMESTAMP, FLAGS, TEXT) VALUES (?, ?, current_timestamp, ?, ?);', (g.UID, g.LID, flags_out, report_text,)
        ).fetchone()

        if error is None:
            session.clear()
            return redirect(url_for('index'))

    else:
        if 'rules' not in globals():
            global rules
            with open('rules.txt') as f:
                rules = list(f.readlines())
        else:
            global rules

        return render_template('report/create.html', rules=rules)
    