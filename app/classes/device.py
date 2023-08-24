from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DeviceForm(FlaskForm):
    hostname = StringField('Hostname', validators=[DataRequired()])
    ip_address = StringField('IP Address', validators=[DataRequired()])
    port = StringField('Port', validators=[DataRequired()])
    switch = StringField('Switch', validators=[DataRequired()])
    submit = SubmitField('Add Device')
